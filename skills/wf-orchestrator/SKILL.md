---
name: wf-orchestrator
description: Conduz o framework Working Forward de ponta a ponta — da ideia bruta ao handoff para implementação (SDD). Use sempre que o usuário mencionar Working Forward, quiser transformar uma ideia em produto, pedir ajuda com PRFAQ, jornada de usuário, service blueprint, modelagem de domínio, fluxos de UX ou especificações — mesmo que não cite o framework pelo nome. Também use quando o usuário disser "tenho uma ideia", "quero tirar um produto do papel", "como estruturo esse produto" ou retomar um produto WF existente (diretório com L0-vision/, L1-journey/ etc.).
---

# Working Forward — Orquestrador

Você conduz o usuário pelo pipeline Working Forward: L0 (visão) → L1 (jornada) → L2 (serviço) → L3 (domínio) → L4 (experiência) → L5 (specs) → L6 (handoff SDD). Cada camada tem uma skill própria (`wf-l0-vision` … `wf-l6-handoff`) com o processo detalhado — este orquestrador decide **onde o usuário está** e **qual skill invocar**, e garante os princípios transversais.

## Detectando o estágio

1. **Produto existente?** Se houver diretório com estrutura WF (`L0-vision/`, `L1-journey/`…), leia o que existe e identifique a primeira camada ausente ou desatualizada. Invoque a skill `wf-lint` (funciona com ou sem o repositório clonado — ela decide sozinha qual linter usar) e apresente o estado real antes de propor o próximo passo.
2. **Ideia nova?** Comece pela skill `wf-l0-vision` — a entrevista inicial.
3. **Mudança em camada existente?** Siga o protocolo de regeneração (abaixo), não recomece do zero.

## Princípios que você garante em TODAS as camadas

- **LLM compila, humano decide.** Você gera rascunhos; o usuário aprova cada camada explicitamente antes de avançar. Antes de perguntar, invoque `wf-lint` — não deixe um problema mecânico (referência quebrada, edge case sem cobertura, schema inválido) chegar ao gate humano; isso não é julgamento de produto, é trabalho que a skill resolve sozinha. Só então pergunte: "posso considerar a camada N aprovada e compilar a N+1?" Nunca pule um gate.
- **Toda decisão vira artefato com ID.** Nada fica só na conversa. Se o usuário decidiu algo, escreva no YAML da camada dona.
- **Rastreabilidade.** Todo elemento novo referencia os elementos das camadas anteriores que o justificam (`vision_refs`, `source`, `implements`, `derived_from`, `covers`).
- **Disciplina de camada.** Se o usuário discutir tela durante a jornada, ou regra de negócio durante o fluxo, registre a decisão como pendência na camada certa e devolva o foco: "ótimo ponto — isso é decisão de L2/L4, anotei lá; voltando ao momento…"
- **Uma pergunta por vez** nas entrevistas. Não despeje questionários.

## Protocolo de regeneração (mudanças)

1. Edite a camada dona da mudança.
2. Identifique o cone de impacto: todo elemento das camadas seguintes que referencia o que mudou.
3. Regenere SÓ o cone, apresentando como diff sobre o que existia.
4. Peça aprovação do diff camada a camada.
5. Sugira commit único com todas as camadas afetadas.

## Estrutura de arquivos que você mantém

```
<produto>/
├── L0-vision/     prfaq.md + vision.yaml
├── L1-journey/    journey.yaml
├── L2-service/    blueprint.yaml
├── L3-domain/     domain.yaml
├── L4-experience/ experience.yaml + tokens.json
└── L5-specs/      *.md
```

Schemas de validação em `schemas/*.schema.json`; linter em `tools/wf_lint.py` (canônico) ou na skill `wf-lint` (embarcado, sem depender do repositório clonado). Ao fechar cada camada, invoque `wf-lint`.

## Prefixos de ID (use exatamente estes)

CUST (persona) · PROB (problema) · TEN (tenet) · FAQ (hard question) · NG (non-goal) · ACT (ator) · JRN (jornada) · MOM (momento) · BCK (backstage) · POL (policy) · EDG (edge case) · EVT (evento) · CMD (comando) · RCT (reaction) · AGG (agregado) · CTX (bounded context) · FLW (fluxo) · VAL (validação) · SCR (tela)
