---
name: wf-lint
description: Valida um produto Working Forward (schemas + coerência entre camadas) rodando o linter — embarcado nesta skill, funciona mesmo sem o repositório clonado. Use depois de compilar ou editar qualquer camada (L0-L5), antes de pedir aprovação de um gate ("posso considerar a camada N aprovada?"), quando o usuário pedir para "validar", "lintar", "checar se está tudo certo" ou "rodar o linter" num produto WF, ou ao retomar um produto existente para saber seu estado real antes de propor o próximo passo.
---

# WF Lint — validação estrutural e de coerência

Esta skill roda o "sistema imunológico" do Working Forward: os 8 checks de `tools/wf_lint.py` (schemas JSON Schema + coerência entre camadas — referências resolvem, hard questions foram consumidas, edge cases estão cobertos no L4, eventos têm emissor/consumidor, validações têm pedigree, specs estão ancoradas, non-goals nunca são servidos por um fluxo). Veja `docs/reference-guide.md` §4.3 para o que cada check garante.

**Por que essa skill existe.** `python tools/wf_lint.py` só funciona de graça no Claude Code, que tem acesso direto ao disco via Bash. No claude.ai e no Claude Desktop sem acesso a pasta liberado, não existe "o repositório" — só o que está na conversa. Esta skill resolve isso embarcando uma cópia autocontida do linter e dos 5 schemas em `scripts/`, para funcionar em qualquer ambiente que tenha execução de código Python.

## Como decidir qual linter rodar

1. **Existe um checkout do repositório Working Forward acessível?** (ex.: você está no Claude Code, ou no Desktop com acesso a uma pasta que contém `tools/wf_lint.py`). Se sim, **prefira o canônico**: `python3 tools/wf_lint.py <caminho-do-produto>`. É a fonte da verdade; a cópia embarcada pode ficar desatualizada entre releases do framework.
2. **Não há repositório acessível** (claude.ai puro, ou Desktop sem pasta liberada — só o que o usuário colou/anexou na conversa). Use o script embarcado desta skill: `scripts/wf_lint.py`, que já traz os 5 schemas em `scripts/schemas/`. Nesse caso:
   a. Garanta as dependências primeiro (idempotente, seguro rodar sempre): `pip install --quiet pyyaml jsonschema`.
   b. Reconstrua a estrutura de diretórios esperada num diretório de trabalho do ambiente de execução, a partir do que o usuário forneceu:
      ```
      <produto>/
      ├── L0-vision/vision.yaml       (+ prfaq.md, não lido pelo linter)
      ├── L1-journey/journey.yaml
      ├── L2-service/blueprint.yaml
      ├── L3-domain/domain.yaml
      ├── L4-experience/experience.yaml
      └── L5-specs/*.md
      ```
      Camadas ausentes são toleradas (o linter pula checks que dependem delas) — não invente conteúdo só para preencher a estrutura.
   c. Rode `python3 scripts/wf_lint.py <produto>` (ajuste o caminho do script conforme onde a skill foi instalada).

Em ambos os casos, **nunca** interprete a ausência do `jsonschema` como "validação estrutural pulada, tudo bem" — o linter hoje falha alto (`sys.exit`) se a dependência não estiver instalada, de propósito: uma versão anterior retornava verde silencioso nesse caso, o que mascarava produtos com erro de schema real. Se o `pip install` falhar por falta de rede no ambiente de execução, diga isso explicitamente ao usuário — não declare o produto validado sem ter rodado o check `schemas`.

## Lendo o resultado

- `resultado: OK` com todos os checks `✔` → pode propor o próximo gate.
- Qualquer `✖` (nível `commit`) → **bloqueante**. Não peça aprovação do gate até resolver ou até o usuário decidir explicitamente aceitar o risco (ex.: um `edge_case` com `accepted_risk` documentado, não um schema quebrado).
- `⚠` (nível `advisory`) → mostre ao usuário, mas não bloqueie o fluxo; são sinais pra revisão humana, não erros mecânicos.
- Um produto pode **falhar de propósito** e isso ser correto — ver `examples/products/traco/NOTES.md`: um edge case sem `resolution` nem `accepted_risk` porque a decisão de produto por trás dele nunca foi tomada de verdade é mais honesto que forçar uma resolução ou um `accepted_risk` com dono fictício só para o lint passar. Se o usuário disser explicitamente que uma falha é intencional, registre o porquê (num `NOTES.md` do produto, no estilo de `traco`) em vez de insistir em fechá-la.

## Uso dentro do pipeline (via `wf-orchestrator`)

Depois de compilar qualquer camada (L0 a L5), rode esta skill **antes** de perguntar "posso considerar a camada N aprovada?". Um rascunho com referência quebrada ou edge case sem cobertura não deveria nunca chegar ao gate humano — isso é trabalho mecânico que a skill resolve sozinha, deixando a revisão humana focada em julgamento de produto (a pergunta certa é "essa é a jornada que queremos contar?", não "essa jornada.yaml tem YAML válido?"). Isso é evidência concreta, não teórica: `docs/case-study-l0-l1-compilation.md` mostra um rascunho gerado por LLM que validou de primeira contra o schema mas ainda precisou de correções substantivas de julgamento humano — o lint não substitui a revisão, elimina a categoria de erro que a revisão não deveria ter que pegar.
