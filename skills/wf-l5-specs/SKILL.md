---
name: wf-l5-specs
description: Camada L5 do Working Forward — compila TODAS as camadas anteriores em especificações funcionais por feature, em Markdown com cláusulas EARS e referências [ID] inline, produzindo L5-specs/*.md. Use quando L0-L4 estiverem aprovados e for hora de gerar specs, PRD, requisitos ou critérios de aceite num produto WF; ou quando o usuário pedir "gera as specs" ou "prepara pro time de dev / pro Spec Kit / pro Kiro".
---

# WF L5 — Especificação (compilação EARS)

Objetivo: a spec do Working Forward é pouco escrita e muito **derivada**. O trabalho pesado já foi aprovado camada a camada — aqui você junta, com referências. Este é o dividendo do framework: a spec deixa de ser onde tudo se decide às pressas e vira onde tudo se confirma.

## Processo

### 1. Recortar features

Agrupe por valor entregável, tipicamente 1 feature ≈ 1 fluxo ou 1–2 momentos coesos. Cada feature vira um arquivo `L5-specs/<feature>.md` com cabeçalho declarando: momentos servidos, fluxo, contexto de domínio — tudo como referências `[ID]`.

### 2. Derivar cláusulas EARS

Padrões (use exatamente estas keywords — o linter as reconhece):
- `WHEN <evento/gatilho> THE SYSTEM SHALL <comportamento>` — respostas a eventos
- `IF <condição> THEN THE SYSTEM SHALL <comportamento>` — comportamento condicional
- `WHILE <estado> THE SYSTEM SHALL <comportamento>` — comportamento contínuo

Fontes de derivação (nesta ordem):
1. Cada **policy** do L2 → ≥1 cláusula (o on_violation vira cláusula também)
2. Cada **edge case** com resolution → 1 cláusula IF/WHEN
3. Cada **reaction** do L3 → 1 cláusula WHEN evento
4. Cada **transição relevante** do L4 (guards, invokes, must_render de truth_moments) → cláusulas
5. SLAs do L2 → cláusulas de performance

### 3. Ancoragem (o linter bloqueia sem isso)

TODA cláusula termina com referências `[ID]` às camadas que a justificam — mínimo 1, ideal 2–3 (a regra + o momento/fluxo). Cláusula que você não consegue ancorar = escopo inventado na compilação → ou remova, ou volte à camada dona e registre a decisão lá primeiro.

### 4. Revisão leve com o usuário

Apresente feature a feature. As perguntas do gate: "algo aqui te surpreende?" (se sim, alguma camada anterior mentiu — investigue) e "qual a ordem de implementação?" (priorização é a única decisão nova desta camada).

## Gate G5 (checklist)

- [ ] Toda policy do L2 coberta por ≥1 cláusula
- [ ] Todo edge case com resolution coberto
- [ ] Toda cláusula com ≥1 referência [ID]
- [ ] Nenhuma cláusula introduz comportamento sem origem nas camadas
- [ ] Features priorizadas pelo usuário

Rode o linter completo (`python tools/wf_lint.py <produto>`). Ao aprovar: "L5 aprovado — produto pronto pro handoff SDD (L6)."
