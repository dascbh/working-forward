---
name: wf-l3-domain
description: Camada L3 do Working Forward — compila o blueprint (L2) em modelo de domínio estilo EventStorming/DDD, produzindo domain.yaml com eventos, comandos, reactions, agregados e bounded contexts. Use quando existir blueprint.yaml aprovado e for hora de modelar o domínio, ou quando o usuário pedir EventStorming, DDD, bounded contexts, modelagem de eventos ou arquitetura de domínio num produto WF. ATENÇÃO: o gate humano desta camada é o mais crítico do pipeline — fronteiras de contexto têm o maior custo de reversão.
---

# WF L3 — Domínio (EventStorming formalizado)

Objetivo: tirar o EventStorming do post-it. Extrair do blueprint a estrutura conceitual: eventos, comandos, reactions, agregados, bounded contexts.

## Processo

### 1. Compilar rascunho a partir do L2

- **Eventos (EVT-*):** varra o blueprint perguntando "que fato de negócio aconteceu aqui?" Cada backstage relevante emite eventos (`emitted_by: BCK-*`). Nomeie no passado (EVT-ReservaCriada, não EVT-CriarReserva).
- **Comandos (CMD-*):** as intenções que disparam mudanças. `actor` é um ACT-* ou `system`. Todo comando declara `produces`.
- **Reactions (RCT-*):** "quando EVT, então CMD" — e crucialmente, `implements: POL-*`. Reactions são as policies do L2 ganhando mecânica. Policy sem reaction que a implemente merece pergunta.
- **Agregados (AGG-*):** os guardiões de consistência. `invariants` referencia as POL-* que o agregado protege transacionalmente.
- **Contexts (CTX-*):** agrupe agregados por coesão de linguagem e mudança. `moments_served` liga o contexto de volta à jornada. Declare `relationship` entre contextos (upstream/downstream, shared-kernel, published-language...).

### 2. Fechamento de eventos (o linter cobra)

Todo evento precisa de origem (comando que `produces` ou backstage que `emitted_by`) E destino (reaction que consome ou fluxo do L4 que escuta). Evento órfão = modelagem morta ou lacuna real — descubra qual.

### 3. Revisão de fronteiras COM o usuário (não pule)

Para cada fronteira proposta, pergunte:
- "Esses dois conceitos mudam juntos ou por razões diferentes?"
- "A mesma palavra significa coisas diferentes nos dois lados?" (sinal clássico de fronteira)
- "Se isso virar dois serviços/times, a comunicação entre eles é aceitável?"

Apresente o custo: fronteira errada = re-arquitetura. É a decisão mais cara do pipeline — trate como tal.

## Gate G3 (checklist)

- [ ] Todo evento tem emissor e consumidor
- [ ] Toda reaction implementa uma policy nomeada
- [ ] Invariantes de agregado referenciam POL-*
- [ ] Fronteiras justificadas por acoplamento real, não por organograma
- [ ] moments_served cobre todos os momentos da jornada
- [ ] Usuário revisou as fronteiras explicitamente (não aceite aprovação no piloto automático)

Valide contra `schemas/domain.schema.json`. Ao aprovar: "L3 aprovado. Próximo: materializar a experiência (L4) — fluxos como máquinas de estado."
