---
name: wf-l1-journey
description: Camada L1 do Working Forward — compila a visão (L0) em jornadas e momentos no estilo storyboard do Airbnb, produzindo journey.yaml. Use quando existir um vision.yaml aprovado e for hora de mapear a jornada do usuário, momentos, atores e momentos de verdade; ou quando o usuário pedir user journey, jornada do cliente, storyboard ou mapa de experiência num produto WF.
---

# WF L1 — Jornada (storyboarding)

Objetivo: transformar a promessa do L0 numa sequência de momentos vividos por atores reais. Momento ≠ tela: um momento é uma cena com intenção e emoção; telas vêm no L4.

## Processo

### 1. Compilar rascunho a partir do L0

Leia `vision.yaml`. Para cada persona (CUST-*), proponha 1–2 jornadas: a jornada-núcleo (do trigger ao momento aha do PRFAQ) e, se houver persona secundária, a jornada dela. Para cada jornada: `trigger` concreto ("cliente pergunta X", não "usuário tem necessidade"), `shape` (linear ou loop — produtos de uso recorrente têm jornadas loop), e 3–7 momentos.

Para cada momento: `intent` (o que o ator quer NAQUELE instante), `emotion_target` (a emoção que o produto quer produzir — alívio, controle, confiança...), `channel`, `truth_moment` (o produto ganha ou perde o usuário aqui?), `vision_refs` (que PROB/TEN este momento ataca).

### 2. Entrevistar sobre o rascunho

- "Essa é a história que você quer que o cliente conte no bar?"
- Para cada truth_moment proposto: "é aqui mesmo que se ganha ou perde?"
- "Que momento está faltando — antes do primeiro ou depois do último?" (onboarding e pós-uso são os esquecidos clássicos)

### 3. Regras de disciplina

- Se aparecer discussão de tela/botão → anote como pendência de L4 e volte.
- Se aparecer regra de negócio ("mas e se o cliente não pagar?") → anote como candidata a policy/edge case de L2 e volte.
- Momentos sem `vision_refs` são suspeitos: ou a visão está incompleta, ou o momento é enfeite.

## Gate G1 (checklist)

- [ ] Toda persona primária tem jornada
- [ ] Todo momento tem intent + emotion_target
- [ ] truth_moments marcados (1–3 por jornada; se tudo é verdade, nada é)
- [ ] Nenhum momento é uma tela disfarçada ("preencher formulário" é tela; "formular a dúvida" é momento)
- [ ] Jornadas loop identificadas como loop
- [ ] vision_refs presentes nos momentos-chave

Valide contra `schemas/journey.schema.json`. Ao aprovar: "L1 aprovado. Próximo: o iceberg de cada momento — blueprint de serviço (L2)."
