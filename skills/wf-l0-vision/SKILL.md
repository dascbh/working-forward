---
name: wf-l0-vision
description: Camada L0 do Working Forward — transforma uma ideia bruta em visão formal via entrevista, produzindo prfaq.md (estilo Amazon Working Backwards) e vision.yaml. Use quando o usuário tiver uma ideia de produto ainda sem estrutura, pedir um PRFAQ, press release interno, documento de visão, ou quando o orquestrador WF indicar que L0 está ausente ou incompleto. Use mesmo que o usuário chegue só com "tenho uma ideia de app/produto/serviço".
---

# WF L0 — Visão (Working Backwards)

Objetivo: extrair do usuário, por entrevista, o suficiente para escrever um PRFAQ digno de revisão — e dele derivar o `vision.yaml` estruturado.

## Processo

### 1. Entrevista (uma pergunta por vez, nesta ordem de prioridade)

1. **Cliente:** "Quem exatamente é a pessoa que mais sofre o problema? Descreva o dia dela." (não aceite "empresas" — exija a pessoa)
2. **Problema:** "O que ela faz hoje sem o seu produto? Quanto custa — em tempo, dinheiro ou risco?" Peça evidência: "como você sabe? viu, mediu, entrevistou?"
3. **Solução em uma frase:** "Se o produto só pudesse fazer UMA coisa, qual seria?"
4. **Momento aha:** "Qual é o instante em que o cliente pensa 'nunca mais volto pro jeito antigo'?"
5. **Tenets:** "Que princípio você não trai nem sob pressão comercial?" (1–3, não mais)
6. **North star:** "Que número, subindo, prova que o produto funciona?"
7. **Hard questions:** provoque você mesmo — proponha 3–6 perguntas difíceis que a ideia levanta (conflitos, falhas, abusos, limites) e pergunte se doem. As boas viram `hard_questions` com `owner_layer`.
8. **Non-goals:** "O que este produto deliberadamente NÃO é?" (proteja o escopo)

### 2. Gerar o prfaq.md

Press release de ~1 página (data fictícia, cliente nomeado, problema, solução, uma citação plausível) + FAQ externa (2–4 perguntas de cliente) + FAQ interna listando as hard questions com a camada dona de cada uma.

### 3. Extrair o vision.yaml

Siga `schemas/vision.schema.json`. Toda hard question ganha `owner_layer` (L2 para regras de negócio e falhas operacionais; L4 para dilemas de experiência; L3 para questões de modelo). Severidade dos problemas com base na evidência declarada.

## Gate G0 (checklist antes de aprovar)

- [ ] Cliente é uma pessoa nomeável, não uma categoria abstrata
- [ ] Todo problema tem severidade E evidência
- [ ] Solution one-liner cabe em 280 chars e um leigo entende
- [ ] 1–3 tenets que realmente cortam decisões (teste: "esse tenet já proibiria alguma feature óbvia?")
- [ ] Toda hard question tem owner_layer
- [ ] Pelo menos 1 non-goal
- [ ] O press release seria constrangedor se fosse mentira? (se não, é vago demais)

Ao aprovar, diga: "L0 aprovado. Próximo passo: compilar a jornada (L1) — quer seguir?"
