---
name: wf-l4-experience
description: Camada L4 do Working Forward — compila blueprint (L2) e domínio (L3) em experiência formal, produzindo experience.yaml (fluxos como máquinas de estado, telas, validações com pedigree) e tokens.json (W3C Design Tokens). Use quando L2/L3 estiverem aprovados e for hora de desenhar fluxos, telas, estados, validações de interface ou design tokens; ou quando o usuário pedir UX flows, wireflow, statechart de interface, design system ou "como fica na tela" num produto WF.
---

# WF L4 — Experiência (statecharts + tokens)

Objetivo: materializar momentos em fluxos, fluxos em estados, estados em telas — com a decisão estrutural do framework: **fluxos são máquinas de estado**, não sequências de imagens. O caminho triste é um estado nomeado com tela digna, não o slide 47 que ninguém desenhou.

## Processo

### 1. Compilar fluxos a partir de L1+L2+L3

Para cada jornada (ou grupo de momentos coesos), um FLW-*:
- `serves`: os MOM-* que o fluxo materializa
- `states`: cada estado com `screen` (SCR-*), transições em `on`
- **Amarração ao domínio:** estados que disparam ação usam `invoke: CMD-*`; transições escutam EVT-* do L3. A UI e o domínio falam a mesma língua.
- **Cobertura de edge cases:** todo EDG-* do L2 (sem accepted_risk) aparece em `covers` de algum estado ou transição. O linter bloqueia commit sem isso.
- **Hard questions de L4:** FAQ-* com owner_layer L4 são respondidas aqui — use campo `answers: [FAQ-*]` no estado que as resolve.
- `must_render`: o contrato mínimo da tela naquele estado (derivado do frontstage do L2). Não é layout — é o que NÃO PODE faltar.

### 2. Validações com pedigree

Toda VAL-* declara `derived_from: POL-* ou EDG-*`. Validação sem pedigree é decisão clandestina — o linter bloqueia. Se uma validação parece necessária mas não tem origem, a origem está faltando no L2: volte lá (protocolo de regeneração), não invente aqui.

### 3. Telas e tokens

- SCR-* com `components` (nomes semânticos, não biblioteca) e `tokens_scope`.
- `tokens.json` no formato W3C Design Tokens: cores (brand + semantic), tipografia, espaçamento. Tokens semânticos nomeiam INTENÇÃO (verified, caveat, danger), não aparência.

### 4. Revisão com o usuário (as duas perguntas do gate)

1. "Cada momento de verdade da jornada tem o cuidado que merece?" — percorra os truth_moments e mostre o estado/tela correspondente.
2. "Cada estado triste tem uma tela digna?" — percorra os estados que cobrem EDG-* de severidade alta.

## Gate G4 (checklist)

- [ ] Todo momento da jornada é servido por algum fluxo
- [ ] Todo EDG-* coberto (covers) ou accepted_risk
- [ ] Toda transição de ação amarrada a CMD/EVT do domínio
- [ ] Toda validação com derived_from válido
- [ ] must_render derivado do frontstage do L2
- [ ] Tokens semânticos para os estados de verificação/erro/pendência que o produto tem

Valide contra `schemas/experience.schema.json`. Ao aprovar: "L4 aprovado. Próximo: compilar as specs (L5) — agora é quase automático."
