---
name: wf-l2-service
description: Camada L2 do Working Forward — compila a jornada (L1) em service blueprint estilo Uber, produzindo blueprint.yaml com frontstage, backstage, políticas de negócio e edge cases. Use quando existir journey.yaml aprovado e for hora de mapear regras de negócio, validações, exceções, casos de falha, SLAs e operação; ou quando o usuário pedir service blueprint, regras de negócio, edge cases ou "o que acontece quando dá errado" num produto WF. Esta é a camada onde o agente tem alavancagem máxima: enumere edge cases exaustivamente.
---

# WF L2 — Serviço (blueprint + regras + edge cases)

Objetivo: expor o iceberg de cada momento. Esta é a camada mais valiosa do pipeline — é onde mora quase tudo que as specs perdem. Divisão de trabalho explícita: **você enumera exaustivamente; o usuário decide as resoluções.**

## Processo

### 1. Compilar rascunho por momento (priorize truth_moments)

Para cada momento do `journey.yaml`:
- **frontstage:** o que o usuário vê/recebe (sem desenhar tela — isso é L4)
- **backstage (BCK-*):** o que sistema e operação fazem; marque `human: true` para processos humanos; proponha `sla_ms` onde latência importa
- **policies (POL-*):** regras de negócio com `source` (TEN/FAQ/PROB do L0) e `on_violation` obrigatório — regra sem consequência não é regra
- **edge_cases (EDG-*):** AQUI está seu superpoder. Enumere SEM PUDOR, por categoria:
  - concorrência (dois usuários, mesmo recurso)
  - timing (expirou, chegou cedo, fuso, feriado)
  - dados (vazio, gigante, malformado, duplicado, desatualizado)
  - terceiros (API fora, fonte oficial fora do ar, pagamento recusado)
  - humanos (não apareceu, desistiu no meio, abusou, errou)
  - escala (volume atípico, pico)

### 2. Consumir as hard questions

Toda FAQ-* do L0 com `owner_layer: L2` DEVE virar policy ou edge case aqui, referenciando o FAQ no campo `source` ou no texto. O linter cobra isso.

### 3. Decisões com o usuário

Para cada edge case, apresente 2–3 resoluções possíveis com trade-offs e pergunte. Aceite `accepted_risk` (com owner, date, reason) para o que for consciente demais adiar — risco aceito com dono é decisão; risco ignorado é bomba.

## Gate G2 (checklist)

- [ ] Todo truth_moment tem blueprint
- [ ] Toda hard question de L2 respondida como policy/edge case
- [ ] Toda policy tem source e on_violation
- [ ] Todo edge case tem resolution OU accepted_risk com dono e data
- [ ] SLAs declarados onde latência é experiência
- [ ] Edge cases de severidade alta revisados um a um com o usuário

Valide contra `schemas/blueprint.schema.json`. Ao aprovar: "L2 aprovado. Próximo: extrair o modelo de domínio (L3) — eventos, comandos e fronteiras."
