# Working Forward

**Um framework de Product Engineering para a era dos agentes — da visão ao código, por camadas formais.**

A Amazon ensinou o mundo a trabalhar *de trás pra frente* até a visão (Working Backwards). Este framework define como trabalhar *pra frente* a partir dela: visão → jornada → serviço → domínio → experiência → especificação → código, com cada camada como um **artefato versionável**, legível por humanos e por agentes de IA, com rastreabilidade ponta a ponta.

> A IA generativa resolveu as duas pontas (ideia→narrativa e spec→código, via SDD).
> O Working Forward formaliza o meio: **design de produto como representação intermediária (IR)**.

📄 **[Reference Guide completo →](docs/reference-guide.md)**

## As camadas

```
L0  VISÃO         prfaq.md + vision.yaml        (Amazon — Working Backwards)
L1  JORNADA       journey.yaml                  (Airbnb — storyboarding)
L2  SERVIÇO       blueprint.yaml                (Uber — service blueprint)
L3  DOMÍNIO       domain.yaml                   (DDD — EventStorming)
L4  EXPERIÊNCIA   experience.yaml + tokens.json (design systems + statecharts)
L5  ESPECIFICAÇÃO specs/*.md                    (EARS, derivado das camadas)
L6  ARQUITETURA   → handoff SDD                 (Spec Kit, Kiro, BMAD, fde-kernel)
```

Princípios: toda camada é um contrato · rastreabilidade por IDs · **LLM compila, humano decide** · regeneração com diff · lints entre camadas · pipeline bidirecional · handoff nativo pro ecossistema SDD.

## Estrutura do repositório

```
docs/reference-guide.md      O paper — leia primeiro
schemas/                     JSON Schema de cada artefato (validação estrutural)
tools/wf_lint.py             Linter de coerência entre camadas (validação semântica)
skills/                      Skills para clientes de IA (Claude, etc.) — uma por camada
examples/artifacts/          Exemplos mínimos comentados, por camada
examples/products/           Pseudo-produtos completos, L0→L5
  ├── aurora-tax/            B2B — plataforma de inteligência tributária
  ├── agendai/               B2C — agendamento para barbearias
  └── ponte/                 infraestrutura crítica — coordenação de resposta a crises em tempo real
```

## Quickstart

**1. Validar um produto de exemplo:**

```bash
pip install pyyaml jsonschema
python tools/wf_lint.py examples/products/aurora-tax
```

**2. Começar um produto novo com IA:**

Adicione as skills de `skills/` ao seu cliente de IA (no Claude: Settings → Capabilities → Skills, ou via `/mnt/skills/user` no Claude Code). Depois:

> "Tenho uma ideia de produto, quero rodar o Working Forward"

A skill `wf-orchestrator` detecta o estágio e conduz — da entrevista inicial (L0) ao handoff SDD (L6), camada por camada, com gates de revisão explícitos.

**3. Estrutura de um produto:**

```
meu-produto/
├── L0-vision/     prfaq.md + vision.yaml
├── L1-journey/    journey.yaml
├── L2-service/    blueprint.yaml
├── L3-domain/     domain.yaml
├── L4-experience/ experience.yaml + tokens.json
└── L5-specs/      *.md
```

## O linter

`wf_lint.py` implementa o "sistema imunológico" do framework — verificações mecânicas de coerência entre camadas:

| Check | Regra |
|---|---|
| `refs-resolve` | toda referência cruzada aponta pra um ID existente |
| `hard-questions` | toda hard question do L0 foi consumida pela camada dona |
| `edge-coverage` | todo edge case do L2 vira estado/transição no L4 ou é `accepted_risk` |
| `event-closure` | todo evento do L3 tem emissor e consumidor |
| `validation-pedigree` | toda validação do L4 deriva de policy ou edge case |
| `spec-anchoring` | toda cláusula do L5 referencia ≥1 ID de camada anterior |
| `non-goals` | nenhum fluxo serve um non-goal do L0 |

## Status

**v0.1 — working draft.** Schemas e skills são propostas vivas; feedback, forks e adversarial reviews são o método, não a exceção. Veja [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

MIT
