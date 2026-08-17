# Skills Working Forward

Nove skills que guiam um cliente de IA pelo pipeline completo — da primeira entrevista ao handoff SDD:

| Skill | Camada | O que faz |
|---|---|---|
| `wf-orchestrator` | — | Detecta o estágio, invoca a skill certa, garante gates e o protocolo de regeneração |
| `wf-l0-vision` | L0 | Entrevista a ideia → `prfaq.md` + `vision.yaml` |
| `wf-l1-journey` | L1 | Visão → jornadas e momentos (`journey.yaml`) |
| `wf-l2-service` | L2 | Momentos → blueprint com policies e edge cases (`blueprint.yaml`) |
| `wf-l3-domain` | L3 | Blueprint → eventos, agregados, bounded contexts (`domain.yaml`) |
| `wf-l4-experience` | L4 | Tudo → fluxos como state machines + tokens (`experience.yaml`) |
| `wf-l5-specs` | L5 | Compilação → specs EARS ancoradas (`L5-specs/*.md`) |
| `wf-l6-handoff` | L6 | Specs → pacotes pro Spec Kit / Kiro / BMAD / Claude Code |
| `wf-lint` | — | Roda os 8 checks do linter (schemas + coerência entre camadas) — embarca uma cópia autocontida do `tools/wf_lint.py` e dos schemas, então funciona mesmo sem o repositório clonado |

## Instalação

**Claude (claude.ai / Desktop):** empacote cada pasta como `.skill` (zip da pasta contendo `SKILL.md`) e adicione em Settings → Capabilities → Skills; ou envie o `SKILL.md` num chat e use "Save skill". **Atenção com `wf-lint`:** o zip precisa incluir a subpasta `scripts/` inteira (script + schemas embarcados), não só o `SKILL.md` — sem `scripts/`, a skill não tem o que executar em ambientes sem o repositório à mão.

**Claude Code:** copie as pastas para `~/.claude/skills/` (ou `/mnt/skills/user/` no ambiente gerenciado), ou distribua como plugin. Aqui `wf-lint` normalmente nem precisa do fallback embarcado — o repositório já está no disco, então ela prefere `tools/wf_lint.py` diretamente (ver `wf-lint/SKILL.md`).

**ChatGPT / outros clientes:** o conteúdo dos `SKILL.md` funciona como instrução de sistema/projeto. Para GPTs: crie um GPT "Working Forward" com o `wf-orchestrator` como instructions e os demais SKILL.md anexados como knowledge — o corpo de cada um contém o processo completo da camada. Para `wf-lint` num GPT, anexe também `scripts/wf_lint.py` e `scripts/schemas/*.json` como arquivos de Code Interpreter, já que o GPT precisa dos arquivos de verdade pra executar, não só da descrição.

## Uso típico

> "Tenho uma ideia de produto, quero rodar o Working Forward"

O orquestrador conduz: entrevista (L0) → aprovação → compilação camada a camada, sempre com gate humano explícito entre camadas. Para retomar um produto existente, aponte o diretório.
