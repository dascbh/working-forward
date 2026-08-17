---
name: wf-l6-handoff
description: Camada L6 do Working Forward — handoff do produto compilado (L0-L5) para frameworks de Spec-Driven Development e implementação. Use quando as specs (L5) estiverem aprovadas e for hora de gerar os artefatos de entrada para GitHub Spec Kit, Kiro, BMAD, Claude Code ou outro fluxo SDD; ou quando o usuário pedir "bora implementar", "gera o projeto", "prepara pro Spec Kit/Kiro" ou "handoff pra engenharia" num produto WF.
---

# WF L6 — Handoff SDD

Objetivo: entregar três pacotes ao mundo da implementação: **specs** (entrada do SDD), **proposta de arquitetura** (dos bounded contexts) e **suíte de enforcement** (das policies/invariantes). O Working Forward termina onde o SDD começa.

## Os três pacotes

### 1. Specs adaptadas ao framework-alvo

Pergunte qual o alvo (ou detecte pelo repo). Adaptações:

- **GitHub Spec Kit:** cada `L5-specs/<feature>.md` vira insumo do `/specify`. Gere um `constitution.md` a partir dos tenets (TEN-*) + policies invioláveis (POL-* que são invariantes de agregado) — o Spec Kit usa constitution como princípios do projeto. Mantenha as referências [ID] no texto: elas sobrevivem como comentários rastreáveis.
- **Kiro:** as cláusulas EARS entram direto em `requirements.md` (Kiro é EARS-nativo). O `design.md` do Kiro recebe a proposta de arquitetura (pacote 2). Momentos e fluxos viram contexto no topo de cada requirement.
- **BMAD:** o PRD do BMAD é gerado de L0+L1+L5; o architecture doc de L3; entregue ambos em `docs/` no formato que os agentes do BMAD esperam.
- **Claude Code direto (sem framework):** gere um `CLAUDE.md` do produto com: one-liner, tenets, policies como regras invioláveis, mapa de contextos, e aponte os arquivos das camadas como fonte da verdade.

### 2. Proposta de arquitetura (de L3)

Um `architecture-proposal.md`: cada CTX-* → módulo/serviço candidato; `relationship` entre contextos → contratos de integração (published-language = API/eventos versionados; shared-kernel = biblioteca comum — alerte sobre o acoplamento); AGG-* → limites transacionais; EVT-* → catálogo de eventos (candidato a esquema de mensageria). Deixe explícito: é PROPOSTA — engenharia decide o deploy (monolito modular vs serviços).

### 3. Suíte de enforcement (de L2+L3+L4)

O diferencial do WF: as regras chegam à engenharia como **verificações**, não como prosa.

- `invariants.md` (ou `invariants.toml` se o alvo for fde-kernel): cada POL-* invariante de agregado → invariante nível commit; policies comportamentais → nível advisory.
- **Testes de aceitação esqueleto:** cada cláusula EARS do L5 → um teste nomeado (`test_POL_CIT_01_resposta_bloqueada_sem_citacao`), corpo `TODO`, referência [ID] em docstring. A eval suite nasce das camadas, não é escrita depois do fato.
- **Guards de fluxo:** cada FLW-* pode ser exportado como definição de state machine (XState/statechart JSON) para o front implementar sobre ela, não a partir dela.

## Processo

1. Rode o linter completo — handoff só com lint limpo (ou accepted_risks explícitos no relatório de handoff).
2. Pergunte o framework-alvo e o formato de repo.
3. Gere os três pacotes num diretório `L6-handoff/<alvo>/`.
4. Gere um `HANDOFF.md` sumário: o que está sendo entregue, o que é decisão aberta da engenharia, e a regra de ouro da manutenção — **mudança de produto começa na camada dona (L0-L4), nunca direto na spec ou no código**; aponte o protocolo de regeneração do orquestrador.

## Gate G6 (checklist)

- [ ] Lint limpo ou riscos aceitos documentados no HANDOFF.md
- [ ] Constitution/regras derivadas dos tenets (não inventadas)
- [ ] Todo teste esqueleto referencia [ID]
- [ ] Fronteiras entregues como proposta, com contratos de integração explícitos
- [ ] HANDOFF.md explica o protocolo de mudança
