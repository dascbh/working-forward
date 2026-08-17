# Case study: does "LLM compiles, human approves" hold for L0 → L1?

**What this is.** Working Forward's central claim (P3, section 4.1) is that an LLM compiles a
draft of layer N+1 from layer N, and a human approves it. This document is one concrete trial
of that claim on the L0 → L1 step, run with a controlled information boundary so the result is
real evidence rather than a demo.

**Method.**

1. A fresh context read *only* `skills/wf-l1-journey/SKILL.md` and
   `examples/products/aurora-tax/L0-vision/vision.yaml` + `prfaq.md`. It had never seen the
   committed `L1-journey/journey.yaml`.
2. Following the skill's instructions exactly (step 1 of the skill: "compilar rascunho a partir
   do L0"), it produced an independent draft `journey.yaml` from scratch, saved to
   `/tmp/wf-transcript/journey-draft.yaml`, and validated it against
   `schemas/journey.schema.json` (it validates cleanly, first pass, no schema errors).
3. Only then was the real, committed `examples/products/aurora-tax/L1-journey/journey.yaml`
   read and diffed against the draft, field by field.

No part of the draft was edited after seeing the real file. What follows is the actual
comparison.

---

## 1. The unassisted draft (in full)

```yaml
actors:
  - id: ACT-ADV
    name: "Advogado tributarista sênior"
    persona_ref: CUST-ADV
  - id: ACT-EST
    name: "Estagiário / associado júnior"
    persona_ref: CUST-EST

journeys:
  - id: JRN-CONSULTA-TRIBUTARIA
    actor: ACT-ADV
    trigger: "cliente corporativo manda pergunta sobre aplicação de IBS/CBS numa operação concreta (e-mail ou WhatsApp)"
    shape: loop
    moments:
      - id: MOM-TRIAGEM-CONSULTA
        name: "Entender a pergunta real"
        intent: "entender exatamente o que o cliente está perguntando e o contexto da operação, separando a dúvida jurídica do ruído"
        emotion_target: "clareza"
        channel: [email]
        truth_moment: false
        vision_refs: [PROB-01]
      - id: MOM-CONSULTA-AURORA
        name: "Formular a dúvida para o Aurora"
        intent: "formular a dúvida em termos que o Aurora Tax consiga responder com precisão, sem precisar vasculhar a base normativa manualmente"
        emotion_target: "expectativa"
        channel: [app]
        truth_moment: false
        vision_refs: [PROB-01]
      - id: MOM-RESPOSTA-FUNDAMENTADA
        name: "Receber a resposta fundamentada"
        intent: "obter uma resposta em minutos com cada afirmação amarrada a um dispositivo normativo verificado e clicável, não uma paráfrase de memória"
        emotion_target: "alívio"
        channel: [app]
        truth_moment: true
        vision_refs: [PROB-02, TEN-01]
      - id: MOM-VALIDA-FONTES
        name: "Conferir as fontes antes de assinar"
        intent: "abrir os links citados e confirmar que a fonte primária realmente sustenta a afirmação antes de colocar o nome embaixo"
        emotion_target: "segurança"
        channel: [app]
        truth_moment: false
        vision_refs: [PROB-02, TEN-01]
      - id: MOM-ENVIA-PARECER
        name: "Entregar o parecer ao cliente"
        intent: "entregar ao cliente corporativo uma resposta que resiste a auditoria, em minutos em vez de dias"
        emotion_target: "confiança"
        channel: [email]
        truth_moment: true
        vision_refs: [north_star, PROB-02]
      - id: MOM-RECUSA-FORA-ESCOPO
        name: "Recusar o que não é fundamentação"
        intent: "lidar com um pedido do cliente que extrapola o escopo (ex.: pedir que o Aurora redija a petição) sem parecer que o produto travou"
        emotion_target: "confiança apesar do não"
        channel: [app]
        truth_moment: true
        vision_refs: [NG-01, TEN-02]

  - id: JRN-TRIAGEM-JUNIOR
    actor: ACT-EST
    trigger: "consulta de cliente cai na caixa compartilhada do escritório e precisa ser triada antes de chegar ao sênior"
    shape: linear
    moments:
      - id: MOM-RECEBE-DEMANDA
        name: "Classificar a demanda"
        intent: "identificar se a pergunta é sobre IBS/CBS e qual o nível de urgência antes de escalar"
        emotion_target: "controle"
        channel: [email]
        truth_moment: false
        vision_refs: [PROB-01]
      - id: MOM-PESQUISA-PRELIMINAR
        name: "Rodar a pesquisa preliminar"
        intent: "rodar a pergunta no Aurora Tax para montar um rascunho de fundamentação antes de escalar ao sênior"
        emotion_target: "competência"
        channel: [app]
        truth_moment: true
        vision_refs: [PROB-01, PROB-02]
      - id: MOM-MONTA-RASCUNHO
        name: "Montar o rascunho fundamentado"
        intent: "organizar a resposta preliminar com as citações que o Aurora trouxe, pronta para revisão do sênior"
        emotion_target: "confiança"
        channel: [app]
        truth_moment: false
        vision_refs: [PROB-02]
      - id: MOM-ESCALA-SENIOR
        name: "Escalar para o sênior"
        intent: "entregar o rascunho fundamentado ao advogado sênior sem parecer que 'chutou' a resposta"
        emotion_target: "alívio"
        channel: [app, email]
        truth_moment: true
        vision_refs: [north_star]
```

Full file: `/tmp/wf-transcript/journey-draft.yaml`.

## 2. The real, committed version

```yaml
actors:
  - { id: ACT-ADV, name: "Advogado", persona_ref: CUST-ADV }
  - { id: ACT-EST, name: "Estagiário", persona_ref: CUST-EST }

journeys:
  - id: JRN-CONSULTA
    actor: ACT-ADV
    trigger: "cliente pergunta sobre incidência de IBS/CBS em operação específica"
    shape: linear
    moments:
      - id: MOM-01
        name: "Formular a dúvida"
        intent: "traduzir a pergunta do cliente em consulta técnica precisa"
        emotion_target: confiança
        channel: [web]
        truth_moment: false
        vision_refs: [PROB-02]
      - id: MOM-02
        name: "Aguardar com visibilidade"
        intent: "saber que a consulta está sendo processada e quanto falta"
        emotion_target: tranquilidade
        channel: [web]
        truth_moment: false
      - id: MOM-03
        name: "Receber resposta fundamentada"
        intent: "obter resposta com base normativa citada e verificável"
        emotion_target: alívio
        channel: [web]
        truth_moment: true
        vision_refs: [PROB-01, PROB-02, TEN-01]
      - id: MOM-04
        name: "Auditar a fundamentação"
        intent: "clicar em cada citação e confirmar a fonte antes de repassar ao cliente"
        emotion_target: segurança
        channel: [web]
        truth_moment: true
        vision_refs: [TEN-01]

  - id: JRN-MONITOR
    actor: ACT-EST
    trigger: "início do dia de trabalho — checar o que mudou no cenário normativo"
    shape: loop
    moments:
      - id: MOM-10
        name: "Revisar o radar do dia"
        intent: "ver as normas novas/alteradas relevantes pros clientes do escritório"
        emotion_target: controle
        channel: [web, email]
        truth_moment: true
        vision_refs: [PROB-01]
      - id: MOM-11
        name: "Encaminhar impacto ao responsável"
        intent: "marcar a norma como relevante e notificar o advogado da conta"
        emotion_target: eficiência
        channel: [web]
        truth_moment: false
```

## 3. Field-by-field diff

### Actors

| Field | Draft | Real | Verdict |
|---|---|---|---|
| IDs | ACT-ADV, ACT-EST | ACT-ADV, ACT-EST | match |
| persona_ref | CUST-ADV / CUST-EST | CUST-ADV / CUST-EST | match |
| name | "Advogado tributarista sênior" / "Estagiário / associado júnior" | "Advogado" / "Estagiário" | draft is more verbose; real is terser. Cosmetic, human would trim. |

### Journey 1 — primary persona (ACT-ADV)

| | Draft: `JRN-CONSULTA-TRIBUTARIA` | Real: `JRN-CONSULTA` |
|---|---|---|
| trigger | "cliente corporativo manda pergunta sobre aplicação de IBS/CBS numa operação concreta (e-mail ou WhatsApp)" | "cliente pergunta sobre incidência de IBS/CBS em operação específica" |
| **shape** | **loop** | **linear** — direct contradiction |
| moment count | 6 | 4 |

Moment-level:

- **MOM-TRIAGEM-CONSULTA** (draft) — no counterpart in real. Real collapses "understand the
  question" and "formulate the query" into a single moment.
- **MOM-CONSULTA-AURORA** (draft) ≈ **MOM-01 "Formular a dúvida"** (real) — same idea, real
  version is the more disciplined single moment. `vision_refs` differ: draft ties this step to
  `PROB-01` (time cost), real ties it to `PROB-02` (audit-trail integrity) — a defensible but
  different judgment call about which problem this moment addresses.
- **(none in draft)** vs **MOM-02 "Aguardar com visibilidade"** (real) — real invents a
  wait-state/system-status moment that has **no textual anchor anywhere in vision.yaml or
  prfaq.md**. It is pure product judgment, not something "compiled" from L0 content. The draft,
  working strictly from the L0 text, never produced this moment. Its absence in the draft isn't
  a compiler failure so much as proof that this moment cannot be derived from L0 alone. Note also
  it correctly has no `vision_refs` — this is a case where the schema field is legitimately empty.
- **MOM-RESPOSTA-FUNDAMENTADA** (draft) ≈ **MOM-03 "Receber resposta fundamentada"** (real) —
  **strong match**: same `emotion_target` (alívio), same `truth_moment: true`, near-identical
  `intent` wording. This is the single cleanest hit in the whole exercise, and it is also the
  moment that is arguably the actual "aha" of the PRFAQ. Real's `vision_refs` include `PROB-01`
  in addition to what the draft had (`PROB-02, TEN-01`) — real is more complete here.
- **MOM-VALIDA-FONTES** (draft) ≈ **MOM-04 "Auditar a fundamentação"** (real) — intent and
  `emotion_target` (segurança) match closely, but **`truth_moment` is flipped**: draft called it
  `false`, real calls it `true`. This is not cosmetic — it is exactly the kind of "é aqui mesmo
  que se ganha ou perde?" judgment call the skill's interview step (step 2) exists to catch. The
  draft under-weighted the audit step as routine; the real version (correctly, arguably) treats
  it as make-or-break: a lawyer who catches a bad citation here is saved, one who doesn't and
  ships it is burned.
- **MOM-ENVIA-PARECER** (draft) — no counterpart in real. The real journey ends at the audit
  step and never storyboards actually delivering the parecer to the client, despite
  `north_star` being defined in terms of "consultas resolvidas."
- **MOM-RECUSA-FORA-ESCOPO** (draft) — no counterpart in real. This is the most consequential
  single omission on the real side: `prfaq.md` explicitly states **"FAQ-13 ... respondida na
  jornada e experiência via recusa com redirecionamento."** The PRFAQ promises the refusal is
  answered *at the journey layer*, but the committed `journey.yaml` contains no refusal moment
  anywhere. The unassisted draft — reading the same PRFAQ — did add exactly this moment. On this
  one point, the draft is more faithful to L0 than the artifact that was actually approved and
  committed.

### Journey 2 — secondary persona (ACT-EST)

This is where the exercise stops being a story about wording and becomes a story about
disagreement over content.

| | Draft: `JRN-TRIAGEM-JUNIOR` | Real: `JRN-MONITOR` |
|---|---|---|
| trigger | "consulta de cliente cai na caixa compartilhada do escritório e precisa ser triada antes de chegar ao sênior" | "início do dia de trabalho — checar o que mudou no cenário normativo" |
| shape | linear | loop |
| topic | reactive: triaging inbound client questions | proactive: daily norm-radar monitoring |
| moment overlap with real | 0 of 4 | 0 of 2 |

These are **two different jobs for the same persona**, not two phrasings of the same journey.
The draft followed `vision.yaml`'s literal persona text — CUST-EST's `context` field says
verbatim "faz a triagem e a pesquisa preliminar das consultas" (does triage and preliminary
research of consultations) — and storyboarded exactly that: inbound-question triage. The real
committed journey instead assigns the intern a proactive monitoring job, derived from `PROB-01`
("monitorar 40+ normas/semana manualmente consome horas de profissional sênior") rather than
from the persona's stated `context` field. Both readings are defensible from the L0 text; they
are not the same journey. A second independent compile of the same L0 document produced a
materially different L1 artifact for this persona — not a variant, a different journey with zero
moment-level overlap.

The draft did get the **loop/linear pattern right in spirit** — it correctly identified that
*some* journey in this product should be `loop` (recurring, cyclical) — but assigned `loop` to
the wrong journey (the per-consultation journey, which is genuinely linear per-instance even
though the product is used repeatedly) instead of to the monitoring journey, which really is
structurally cyclical (scan → triage → repeat, within one sitting). This is the single most
instructive schema-level miss: "loop" describes a journey's own internal shape, not "this
happens more than once," and the draft conflated the two.

---

## 4. What a human reviewer would concretely have had to fix in the draft

1. **Flip `shape` on both journeys** — `loop`→`linear` on the consultation journey, and, had the
   draft's secondary journey been kept, decide it should have been `loop` too (it wasn't, in
   real).
2. **Merge MOM-TRIAGEM-CONSULTA and MOM-CONSULTA-AURORA** into a single "Formular a dúvida"
   moment — the draft split what the real version treats as one moment.
3. **Add "Aguardar com visibilidade"** — a moment with no anchor in L0 at all; purely a product
   instinct a human (or a different prompt) has to supply.
4. **Flip `truth_moment` on the source-verification moment** from `false` to `true` — a real
   judgment correction, not formatting.
5. **Cut MOM-ENVIA-PARECER and MOM-RECUSA-FORA-ESCOPO** from the primary journey to match the
   real scope — or, arguably, **keep MOM-RECUSA-FORA-ESCOPO and add it to the real file**, since
   the PRFAQ explicitly promises this is where FAQ-13 gets answered and the committed file
   currently doesn't deliver on that promise.
6. **Replace the entire secondary journey** — not edit it, replace it. `JRN-TRIAGEM-JUNIOR` and
   `JRN-MONITOR` share zero moments; a reviewer would have to throw away the draft's second
   journey and write a new one, or go back to the L0 author and ask which job the intern actually
   has (triage vs. monitoring), because `vision.yaml` currently supports either reading.
7. **Trim actor names** to the terser committed style (cosmetic).
8. **Standardize moment IDs** from descriptive slugs (`MOM-RESPOSTA-FUNDAMENTADA`) to the
   project's actual convention (`MOM-03`) — cosmetic, but real, since the schema itself has no
   opinion and the draft guessed a different local convention than the one in use.

Item 6 is the one that matters: it is not a correction, it is a rewrite of half the file's
substantive content, triggered by an ambiguity in the L0 document itself.

---

## 5. Honest verdict

The central claim held up about half as well as "compile, then approve" suggests, and it broke
in an instructive rather than a trivial way. On the primary persona's journey, the unassisted
draft was genuinely good: it validated against the schema on the first try, it independently
reconstructed two of the real file's four moments almost word for word — including the correct
`emotion_target` and, once, the correct `truth_moment` call — and it even caught something the
committed, human-approved artifact itself is missing (a refusal moment for FAQ-13 that the PRFAQ
explicitly promises the journey layer will deliver). That is real evidence the compile step does
useful, non-random work and is worth the seconds it takes to run. But "approves" is the wrong
verb for what a human would actually have had to do to this draft. A reviewer would have had to
reverse a structural call (which journey is the loop), flip a truth-moment judgment that changes
where the product's win/loss is claimed to happen, invent a moment with no textual basis in L0 at
all, and — the part that matters most — throw out and rewrite the entire secondary-persona
journey, because the L0 vision document is genuinely ambiguous about what job the secondary
persona does, and two independent compiles of the same input resolved that ambiguity in
mutually exclusive ways. That last failure is not a wording nit a human fixes in thirty seconds;
it is the kind of disagreement that sends you back to the L0 author, i.e., back up a layer, not
just down through a review gate. On this one trial, "LLM compiles, human approves" is true for
roughly one journey's worth of the file and false for the other: the framework's real shape, at
least here, is closer to "LLM proposes a structurally valid but partially wrong draft; human
substantively rewrites at least one full journey and reverses at least two explicit judgment
calls before it is committable" — which is a materially heavier claim than "approves," and the
paper should say so rather than imply a rubber stamp is usually enough.

---

## Appendix: artifacts

- Draft (produced before reading the real file, unedited since):
  `/tmp/wf-transcript/journey-draft.yaml`
- Schema validation: `python3 -c "import yaml, json, jsonschema; ..."` against
  `schemas/journey.schema.json` — **PASS**, no errors, on first generation.
- Real committed file used for comparison:
  `examples/products/aurora-tax/L1-journey/journey.yaml`
- Source layer read to produce the draft:
  `examples/products/aurora-tax/L0-vision/vision.yaml`,
  `examples/products/aurora-tax/L0-vision/prfaq.md`
- Skill followed: `skills/wf-l1-journey/SKILL.md`
