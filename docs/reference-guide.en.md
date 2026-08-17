> 🇧🇷 Versão original em português: [`reference-guide.md`](reference-guide.md)

# Working Forward
## A Product Engineering framework for the age of agents — from vision to code, through formal layers

**Version 0.1 — Reference Guide / Working Paper**
August 2026

---

## Abstract

Generative AI has solved both ends of product development. At the front end, turning an idea into narrative — PRFAQ, pitch, vision document — has become trivial. At the back end, turning a specification into code has too: the Spec-Driven Development ecosystem (Spec Kit, Kiro, BMAD, Tessl) has consolidated the spec → plan → tasks → implementation loop. What remains unsolved is the middle: translating vision into **product** — journeys, flows, screen states, business rules, validations, domains, and experience — before any technical specification can make sense.

Historically, this middle ground never had a single framework. The world's best product organizations (Amazon, Airbnb, Uber, Netflix) solved slices of it with their own artifacts — Working Backwards and the PRFAQ, journey storyboarding, service blueprinting, experimentation at scale — and the software community contributed Domain-Driven Design and EventStorming. In parallel, engineering already had formal, machine-readable notations for pieces of this same middle ground — Context Mapper for domain boundaries, XState/SCXML for UI state machines, BPMN for process, Gherkin for acceptance criteria — but each was isolated in an engineer's tool, never stitched together and never adopted by the people who design product. In both cases, every arrow between artifacts was always a manual translation, with information loss, performed by senior professionals, and never versioned as a contract.

**Working Forward** proposes formalizing this entire pipeline as a chain of versionable artifacts, readable by humans and AI agents alike, with end-to-end traceability and LLM-assisted regeneration between layers. The name is deliberate: Amazon taught us to work *backwards* to the vision (Working Backwards); this framework defines how to work *forward* from it — from vision to code, without any intermediate layer living only in someone's head.

---

## 1. The problem: the valley between vision and spec

### 1.1 What the SDD era solved — and what it ignores

Spec-Driven Development established a consensus in 2025–2026: the specification, not the code, is the source of truth. Every mature framework converges on the same four-phase loop — specify, plan, break down into tasks, implement — with the spec as an executable, regenerable contract.

But look at what these specs actually contain: features, acceptance criteria, technical constraints, *system-level* edge cases. They answer "what should the software do." They do not answer:

- **How the user moves through the product** — the journey, its moments, its emotions, its drop-off points.
- **What happens behind the scenes** of each interaction — operations, integrations, human processes that hold up the experience.
- **What business rules govern each step** — validations, policies, exceptions, and what the product does when they fail.
- **How the domain is organized** — which concepts exist, which events matter, where the boundaries between contexts lie.
- **How the experience materializes** — screen flows, states, transitions, components, design tokens.

A functional spec born without these layers inherits implicit decisions — made by no one, nowhere, with no record. The agent implementing the spec fills the gaps with whatever is statistically plausible, not with what is right for *this* product. The result is a phenomenon any team that has adopted SDD recognizes: the code is correct with respect to the spec, and the product is wrong with respect to the intent.

### 1.2 Why the valley exists

The valley between vision and spec exists because the product-design layer never had a **single formal representation, shared by the people who design the product and the people who write the code**. That doesn't mean formalization never existed — for domain and experience in particular, it has existed for decades, just confined to engineering tools that product/design never adopted. Compare:

| Layer | Pre-AI formal representation | Versionable? | Machine-readable? |
|---|---|---|---|
| Vision | PRFAQ, 6-pager | Yes (text) | Partially |
| Journey | Storyboard, journey map | No (image/board) | No |
| Service | Service blueprint | No (diagram) | No |
| Domain | EventStorming (post-its!); Context Mapper/CML (textual DDD DSL, since ~2018) | No (EventStorming) / Yes (CML) | No (EventStorming) / Yes (CML) — but with near-zero adoption outside architecture teams |
| Experience | Figma, prototypes; statecharts (Harel 1987), XState/SCXML | Proprietary (Figma) / Yes, text (XState) | No (Figma) / Yes (XState/SCXML) — but as a front-end engineering tool, outside the product/design vocabulary |
| Functional spec | PRD, Gherkin, EARS | Yes | Yes |
| Code | Code | Yes | Yes |

The three layers in the middle — journey, service, domain — and the experience layer lived mostly on walls of post-its, Miro boards, and Figma files: artifacts rich for humans, opaque to machines, impossible to diff, and disconnected from one another. Where real, machine-readable formalization did exist — Context Mapper for domain, XState/SCXML for experience — it lived inside engineering, in a vocabulary and tooling that product managers and designers never touched, isolated from its neighboring layers. When AI arrived, it automated what had formal representation *shared across both ends* (text at the endpoints) and left untouched what was formalized but isolated, or what was never formalized at all.

### 1.3 The thesis

Working Forward's thesis is not that these layers never had formalism — many times they did. Context Mapper formalizes domain, XState/SCXML formalizes experience, BPMN formalizes process, Gherkin formalizes acceptance criteria. The problem was never the absence of notation; it was **fragmentation**: each formalism was born in isolation, inside an engineer's tool, without reference to neighboring layers, and so was never adopted by the people who design product.

**Working Forward's thesis is that these layers need one continuous intermediate representation (IR)** — not a new notation per layer, but a single chain, with stable identities and cross-references between layers, a set of lints that mechanically verify coherence, and an LLM compiler linking every boundary, usable end to end by people who aren't engineers. A set of structured artifacts, versioned in git, that captures — in a chained way — what the storyboard, the blueprint, EventStorming/Context Mapper, and XState/design systems already captured separately, in such a way that:

1. A human can read, review, and approve each layer.
2. An AI agent can generate the draft of layer N+1 from layer N.
3. A change in any layer propagates in a traceable — and auditable — way through the following layers.
4. Cross-layer lints mechanically detect incoherence (an edge case declared in the blueprint that no flow handles; a domain event that no screen triggers).

The LLM, in this arrangement, is not the author of the product. It is the **compiler between layers** — and the human is the decision gate at every boundary.

---

## 2. Principles

**P1 — Every layer is an artifact, every artifact is a contract.** No implicit decisions. If a business rule exists, it's written in a layer, with an ID. If it isn't written, it doesn't exist — and the lint flags the hole.

**P2 — End-to-end traceability.** Every element carries a stable ID and references the elements from earlier layers that justify it. It must be possible to answer mechanically: "why does this screen exist?" (→ flow → journey moment → PRFAQ FAQ) and "what breaks if I remove this rule?" (→ every screen, spec, and test that references it).

**P3 — LLM as compiler, human as gate.** Generation between layers is the agent's work; approval is the human's work. No layer is considered valid without explicit review. This mirrors what 6-pager reviews did at Amazon — except the draft now costs minutes, not weeks.

**P4 — Regeneration with diff, never rewrite.** When layer N changes, layers N+1..k are *recompiled* and the result is presented as a diff over what existed — preserving the human decisions already made in later layers that don't conflict with the change. This is the same principle as mature SDD ("spec-anchored"), extended across the whole pipeline.

**P5 — Progressive fidelity, constant formality.** The early layers are vague on detail and precise on intent; the later ones are the reverse. But all are equally formal: a storyboard in Working Forward is vague about *screens* and exact about *moments, actors, and emotions*.

**P6 — The pipeline is bidirectional.** The canonical path is forward (vision → code), but the framework also supports the reverse path: extracting the IR from an existing product (code → flows → domain → journey) to bring it into the regime. Real products are born from both directions.

**P7 — Native handoff to the SDD ecosystem.** Working Forward doesn't compete with Spec Kit, Kiro, or BMAD — it feeds them. The framework's last layer *is* the input to SDD frameworks. What they treated as a starting point (the spec, written by someone, somehow), Working Forward treats as compiled, traceable output.

---

## 3. The layers

Working Forward organizes the pipeline into seven layers, L0 through L6. Each has: a purpose, a lineage (the classic artifact it formalizes), a canonical artifact, a typical human owner, and an input/output contract with its neighbors.

```
L0  VISION        prfaq.md + vision.yaml        (Amazon — Working Backwards)
L1  JOURNEY       journey.yaml                  (Airbnb — storyboarding)
L2  SERVICE       blueprint.yaml                (service blueprint — Shostack, 1984)
L3  DOMAIN        domain.yaml                   (DDD — EventStorming)
L4  EXPERIENCE    experience.yaml + tokens      (design systems)
L5  SPECIFICATION specs/*.md                    (PRD, EARS, Gherkin)
L6  ARCHITECTURE  → SDD handoff                 (Spec Kit, Kiro, BMAD, fde-kernel)
```

### L0 — Vision (lineage: Amazon Working Backwards)

**Purpose.** Fix the customer, the problem, the solution in one sentence, and the hard questions — before any product decision.

**Artifacts.** The `prfaq.md` stays narrative, as Amazon always advocated: a one-page press release plus an internal and external FAQ. The narrative is irreplaceable — it's where the thinking happens. But Working Forward adds `vision.yaml`: the structured extraction of what the PRFAQ *claims*, so later layers can reference it.

```yaml
# vision.yaml (extracted from prfaq.md, human-reviewed)
product: aurora-tax
customer:
  primary: { id: CUST-01, who: "senior tax attorney", context: "..." }
problem:
  - { id: PROB-01, statement: "manually monitoring 40+ regulations/week", severity: high }
solution_one_liner: "..."
tenets:
  - { id: TEN-01, rule: "when in doubt, cite the regulatory source — never paraphrase without a link" }
north_star: { metric: "queries resolved without escalation", target: "70% in 12mo" }
hard_questions:          # the FAQs that define scope
  - { id: FAQ-07, q: "what happens when two regulations conflict?", owner_layer: L2 }
non_goals:
  - { id: NG-01, statement: "not a filing/legal-document tool" }
```

Note the `owner_layer` field on hard questions: every hard question from the PRFAQ is *addressed* to a layer. "What happens when two regulations conflict?" isn't answered in the vision — it's answered in the blueprint (L2), as a business rule. The framework's lint verifies that every hard question was consumed by its owner layer. It's the mechanization of what the bar raiser did in the 6-pager review: making sure the hard questions don't evaporate.

**Human gate.** Founder / sponsor / PM. Nothing moves forward without an approved PRFAQ — in this, Working Forward is orthodoxly Amazonian.

### L1 — Journey (lineage: Airbnb storyboarding)

**Purpose.** Turn the vision's promise into a sequence of moments lived by real actors — what Airbnb's Snow White project did by mapping the guest and host journey into frames, and discovering that each frame was a domain of product investment.

**Artifact.** `journey.yaml` — actors, moments, and for each moment: intent, target emotion, channel, and what Airbnb called a "moment of truth" (where the experience wins or loses the user).

```yaml
# journey.yaml
actors:
  - { id: ACT-ADV, name: "Attorney", persona_ref: CUST-01 }
  - { id: ACT-EST, name: "Associate", persona_ref: CUST-02 }
journeys:
  - id: JRN-CONSULTA
    actor: ACT-ADV
    trigger: "client asks about tax incidence in operation X"
    moments:
      - id: MOM-01
        name: "Formulate the question"
        intent: "translate the client's question into a technical query"
        emotion_target: confidence
        channel: [web]
        truth_moment: false
      - id: MOM-03
        name: "Receive a substantiated answer"
        intent: "get an answer with cited regulatory basis"
        emotion_target: relief
        truth_moment: true          # this is where the product wins or loses
        vision_refs: [PROB-01, TEN-01]
```

**What this layer does NOT decide:** screens, buttons, endpoints. A moment isn't a screen — often a moment becomes three screens, or half of one. This discipline (P5) is what keeps the journey stable while the experience iterates.

**Human gate.** Product design + PM. The review question: "is this the story we want the customer to tell?"

### L2 — Service (lineage: service blueprinting — Shostack, 1984)

**Purpose.** For each journey moment, expose the iceberg: what the user sees (frontstage), what the system and operations do (backstage), what **business rules** govern the step, and — crucially — the **edge cases** and failure paths. The technique is Lynn Shostack's (*Harvard Business Review*, 1984) — the original notation separating frontstage from backstage to design services, nearly 25 years before a ride-hailing app existed to illustrate it. Uber is cited here as a teaching example, not an origin: a physical-digital product where drivers cancel, GPS fails, and pricing changes in real time makes the frontstage/backstage separation and treating exceptions as first-class citizens particularly easy to visualize — but the discipline itself is Shostack's blueprint.

**Artifact.** `blueprint.yaml` — per moment: frontstage, backstage, policies, and edge cases with a declared resolution.

```yaml
# blueprint.yaml
blueprints:
  - moment_ref: MOM-03
    frontstage:
      - "answer shown with clickable citations per regulatory provision"
    backstage:
      - { id: BCK-11, action: "RAG over the LC 214/2025 base + infralegal acts", sla_ms: 8000 }
      - { id: BCK-12, action: "citation validated against primary source" }
    policies:                        # business rules WITH identity
      - id: POL-CIT-01
        rule: "every regulatory claim MUST cite a verified provision"
        source: TEN-01               # traces back to the vision's tenet
        on_violation: "answer is blocked and reformulated"
      - id: POL-CONF-01
        rule: "a conflict between regulations shows both + the resolution criterion (hierarchy/chronology/specificity)"
        source: FAQ-07               # the PRFAQ's hard question, answered here
    edge_cases:
      - id: EDG-05
        case: "outdated regulatory base (regulation published <24h ago)"
        resolution: "answer with an explicit currency caveat + schedule priority reindexing"
        severity: high
      - id: EDG-06
        case: "question outside tax scope"
        resolution: "decline with a redirect, citing NG-01"
```

**Why this layer is the heart of the framework.** This is where almost everything functional specs lose lives: validations, policies, exceptions, SLAs, operational dependencies. And it's the layer with the highest LLM leverage: given `journey.yaml`, an agent is excellent at *proposing* edge cases exhaustively (it's an adversarial-case generator by nature) — and terrible at deciding the resolutions, which are business decisions. The P3 division is sharp: the agent enumerates, the human decides.

**Human gate.** PM + ops + senior engineering, together. It's the pipeline's most expensive review — and the cheapest compared to discovering the edge cases in production.

### L3 — Domain (lineage: DDD / EventStorming)

**Purpose.** Extract the system's conceptual structure from the blueprint: business events, commands, aggregates, reaction policies, and the boundaries — bounded contexts — that become architecture boundaries. Brandolini's EventStorming was always the pre-AI artifact closest to a product IR; Working Forward takes it off the post-it wall and puts it in git.

**Artifact.** `domain.yaml`.

```yaml
# domain.yaml
events:
  - { id: EVT-ConsultaRespondida, aggregate: Consulta, emitted_by: BCK-11 }
  - { id: EVT-CitacaoInvalidada, aggregate: Consulta, emitted_by: BCK-12 }
commands:
  - { id: CMD-SubmeterConsulta, actor: ACT-ADV, produces: [EVT-ConsultaSubmetida] }
reactions:                # "policies" in EventStorming vocabulary
  - id: RCT-01
    when: EVT-CitacaoInvalidada
    then: CMD-ReformularResposta
    implements: POL-CIT-01           # traces back to the blueprint's rule
aggregates:
  - { id: AGG-Consulta, invariants: [POL-CIT-01, POL-CONF-01] }
contexts:
  - id: CTX-Consultoria
    aggregates: [AGG-Consulta]
    moments_served: [MOM-01, MOM-03]
  - id: CTX-Monitoramento
    aggregates: [AGG-Norma]
    relationship: { with: CTX-Consultoria, type: upstream-published-language }
```

**The traceability insight:** every `reaction` implements a `policy` from L2; every aggregate `invariant` references named rules. When engineering asks "why does the Consulta aggregate block an answer without a citation?", the answer is mechanical: `POL-CIT-01 ← TEN-01 ← prfaq.md`. The architecture inherits intent with a pedigree.

**Human gate.** Senior engineering / architecture. The bounded contexts decided here become services, modules, and teams — it's the pipeline's most expensive decision to reverse.

### L4 — Experience (lineage: design systems + UI state machines)

**Purpose.** Materialize moments into flows, flows into screens, screens into states — with interface validations derived from business policies, and a visual vocabulary anchored in tokens.

**Artifact.** `experience.yaml` (+ `tokens.json` in the W3C Design Tokens standard). The decisive structural choice: **flows are state machines**, not sequences of images. States, transitions, guards, and effects — the same statechart formalism engineering uses, applied to experience.

```yaml
# experience.yaml
flows:
  - id: FLW-CONSULTA
    serves: [MOM-01, MOM-03]
    initial: composing
    states:
      composing:
        screen: SCR-EDITOR
        on:
          SUBMIT: { target: processing, guard: VAL-INPUT-01 }
      processing:
        screen: SCR-AGUARDE
        invoke: CMD-SubmeterConsulta       # binds to the domain (L3)
        on:
          EVT-ConsultaRespondida: { target: answered }
          EVT-CitacaoInvalidada:  { target: reformulating }   # EDG made visible in the UI
          TIMEOUT_8S: { target: degraded } # honors BCK-11's SLA
      answered:
        screen: SCR-RESPOSTA
        must_render: [clickable_citations]  # frontstage of MOM-03
validations:
  - id: VAL-INPUT-01
    field: consulta.texto
    rule: "non-empty, ≤ 4000 chars, pt-BR language detected"
    derived_from: EDG-06               # out of scope → preventive validation
screens:
  - id: SCR-RESPOSTA
    components: [answer-card, citation-chip, feedback-bar]
    tokens_scope: "consulta.*"
```

**What this formalism buys.** Every edge case from L2 needs to show up as a state or transition in some flow — and that's lintable. The sad path stops being slide 47 that no one ever designed; it's a named state with an associated screen. And the `experience.yaml` + `tokens.json` pair is exactly the contract that design-to-code tools can consume to generate real UI — or, in reverse (P6), the target that a code-to-design extractor produces from an existing front end.

**Human gate.** Product design + front-end. The review asks two things: "does every journey moment of truth get the care it deserves?" and "does every sad state have a screen worthy of it?"

### L5 — Specification (lineage: PRD, EARS, Gherkin)

**Purpose.** Compile the previous layers into functional specs per feature — the artifact the SDD ecosystem expects to receive.

**Artifact.** `specs/*.md`, with acceptance criteria in EARS, generated mostly by compilation. A Working Forward spec is written very little and *derived* a lot: the context comes from the journey, the rules come from the blueprint, the events come from the domain, the flows come from the experience — the spec assembles them, with references.

```markdown
# specs/consulta-fundamentada.md
Feature: Substantiated answer to a query   [MOM-03, FLW-CONSULTA]

WHEN the system emits EVT-ConsultaRespondida
THE SYSTEM SHALL display every regulatory claim with a clickable citation
  verified against the primary source.                    [POL-CIT-01]

WHEN citation validation fails (EVT-CitacaoInvalidada)
THE SYSTEM SHALL transition FLW-CONSULTA to 'reformulating'
  without showing the unverified answer.                  [RCT-01, EDG-05]

IF the query falls outside tax scope
THEN THE SYSTEM SHALL decline with a redirect.             [EDG-06, NG-01]
```

**Human gate.** PM + tech lead. Since almost everything is derived, the review is light — the heavy lifting was already approved layer by layer. This is the framework's dividend: the spec stops being the place where everything gets decided in a rush and becomes the place where everything gets *confirmed*.

### L6 — Architecture and implementation (handoff)

Working Forward ends where SDD begins, handing implementation-layer frameworks three things: the specs (L5) as direct input to Spec Kit/Kiro/BMAD; the bounded contexts (L3) as an architecture proposal; and the named policies and invariants as an **enforcement suite** — in fde-kernel's vocabulary, the product's `invariants.toml`, checkable at loop, commit, and advisory level. The acceptance eval suite is born from L2's policies and L4's states, not from tests written after the fact.

---

## 4. The compiler: LLMs between layers

### 4.1 The six compilations

Every boundary between layers is a compilation operation with its own nature — and a specific division of labor between agent and human:

| Boundary | Operation | The agent is good at | The human decides |
|---|---|---|---|
| L0→L1 | narrative → moments | decomposing the promise into scenes, proposing actors | which moments are real moments of truth |
| L1→L2 | moments → iceberg | **exhaustively enumerating edge cases**, proposing backstage | resolutions, SLAs, business trade-offs |
| L2→L3 | rules → model | extracting events/commands from the blueprint, proposing aggregates | context boundaries (reversal cost!) |
| L3+L2→L4 | model → statecharts | generating flows that cover every edge case, mapping screens | visual hierarchy, moments of care, tone |
| L4+…→L5 | everything → specs | near-total compilation (EARS derived) | confirmation and prioritization |
| L5→L6 | specs → code | what SDD already solved | code review, promotion |

Two boundaries deserve special mention. **L1→L2 is where the LLM has maximum leverage**: enumerating failure modes is adversarial generation, a task at which models are systematically better than humans under deadline pressure — while deciding what to do about each failure is pure business judgment. And **L2→L3 is where the human gate has maximum value**: wrong bounded contexts cost re-architecture; no amount of agent fluency compensates for rubber-stamping this layer.

### 4.2 Regeneration and diff (the change protocol)

Real changes don't start at L0 — they start in the middle ("legal decided the resolution of EDG-05 changes"). The protocol:

1. **Edit the owner layer.** The change is made where the element lives (EDG-05 lives in L2).
2. **Mark the impact cone.** The reference graph identifies everything pointing to EDG-05 in the following layers (L4 states, L5 clauses, L6 tests).
3. **Recompile only the cone.** The agent regenerates the impacted elements, proposing diffs — never rewriting entire layers.
4. **Cascading gates.** Every diff passes through the corresponding layer's human gate. A small diff in L2 might generate trivial diffs in L4/L5 — review is proportional to real impact, not to pipeline size.
5. **Atomic commit.** The entire change — every layer — lands in a single commit/PR. Git history tells the product's story by decisions, not by files.

### 4.3 Cross-layer lints (the immune system)

ID-based traceability enables mechanical coherence verification. The framework's minimal lints:

- **Hard-question coverage:** every `hard_question` from L0 was consumed by its `owner_layer`.
- **Edge-case coverage:** every `EDG-*` from L2 appears in ≥1 state/transition in L4, or is explicitly marked `accepted_risk` (with an owner and a date).
- **Event closure:** every event in L3 is emitted by some backstage step and consumed by some reaction or flow — orphaned events flag dead modeling.
- **Validation anchoring:** every `validation` in L4 derives from a `policy` or `edge_case` — validations without a pedigree are decisions made in the dark.
- **Spec completeness:** every EARS clause in L5 references ≥1 ID from an earlier layer — a clause with no reference is scope invented during compilation.
- **Non-goals respected:** no flow/screen serves a `non_goal` from L0.

These lints run in CI like any other check. In the three-level enforcement vocabulary (loop / commit / advisory): edge-case coverage and validation anchoring are commit-level; the rest can start advisory and harden as the team matures.

---

## 5. Maturity levels

Mirroring SDD's ladder (spec-first / spec-anchored / spec-as-source), Working Forward defines three adoption regimes:

**WF-1 · Vision-First.** The layers are used once, at zero-to-one, to arrive at quality specs — and then the code proceeds on its own. No regeneration, no lints in CI. Minimum cost, real value: even if disposable, the pipeline forces the decisions to exist. Suited to prototypes and market validation.

**WF-2 · Layer-Anchored (the sweet spot).** The layers live in the repository alongside the code, changes follow the regeneration protocol, lints run in CI. The product and its IR evolve together, with drift detected mechanically. This is the recommended regime for production products with a dedicated team.

**WF-3 · IR-as-Source.** The layers are the sole source of truth; specs, acceptance tests, and growing portions of code and UI are generated artifacts. Today this is the frontier — it depends on reliable design-to-code (L4→UI) and mature SDD (L5→code) operating in a chain. It's the framework's long-term bet.

---

## 6. Roles and ceremonies

The framework redefines the **meeting points** more than the roles themselves:

- **Sponsor/Founder** — owns L0. Ceremony: PRFAQ review (inherited from Amazon, intact).
- **Product Manager** — thread through L0–L2 and L5. Stops writing PRDs from scratch and starts curating compilations.
- **Product Designer** — owns L1 and L4. The storyboard goes back to being a central artifact (not a kickoff deck that dies), and Figma becomes a *rendering* of `experience.yaml`, not the source of truth.
- **Senior engineering** — owns L3 and the L2→L3 gate. EventStorming becomes a review session for the `domain.yaml` proposed by the agent, not a two-day post-it workshop.
- **Agents** — one per compilation boundary, with their own prompts and contracts (analogous to BMAD's role separation, but organized by *layer*, not by professional persona).

The central ceremony is the **Layer Review**: analogous to code review, but per layer, with the corresponding gate's checklist. The cultural rule: *don't discuss screens in a journey review, don't discuss business rules in a flow review* — every decision has its layer, and out-of-layer discussions get logged as issues in the correct layer.

---

## 7. Working Forward × the ecosystem

| | Scope | What it formalizes | Relationship to WF |
|---|---|---|---|
| **Working Backwards/PRFAQ** | vision | narrative | absorbed as L0 |
| **Storyboarding (Airbnb)** | journey | nothing (visual) | formalized as L1 |
| **Service Blueprint** | operations | nothing (diagram) | formalized as L2 |
| **EventStorming/DDD** | domain | semi (workshop) | formalized as L3 |
| **Design systems/tokens** | UI | tokens only | extended in L4 (statecharts) |
| **Spec Kit / Kiro / BMAD** | spec→code | specs and tasks | downstream — consume L5 |
| **fde-kernel and similar** | enforcement | invariants | receive policies as invariants |
| **Figma Make / UX Pilot** | prototype | nothing (visual output) | possible renderers of L4 |

The table reads as the paper's thesis in grid form: every row above the middle had the right *content* and no formalization; every row below had formalization and started too late. Working Forward doesn't invent any of these ideas — it invents the **missing column**: continuous formal representation from vision to code.

---

## 8. Limitations and open questions

An honest reference guide states what it doesn't know:

**Ceremony cost.** Seven layers with human gates is real weight. The framework bets that LLM compilation reduces the *production* cost of each layer to the point where *review* cost dominates — and review is exactly where senior humans pay off most. But that bet needs empirical validation; for teams of 2–3 people, WF-1 is a reasonable ceiling.

**YAML expressiveness.** Structured schemas capture decisions, not aesthetic sensibility. L4 formalizes states and validations; it doesn't formalize *why this screen is moving*. The framework mitigates this by keeping narrative and visual artifacts as referenced attachments — but the tension between formality and expressiveness is permanent.

**Compilation fidelity.** The quality of the L(N+1) draft depends on the model, the boundary agent's prompt, and the richness of layer N. The framework needs its own benchmark: given a reference `journey.yaml`, how complete is the generated blueprint? (A direct analogue to SDD evals.)

**Non-transactional products.** Layers L1–L2 assume journeys with a beginning, middle, and end. Continuous-engagement products (feeds, games, creative tools) map worse — the journey becomes loops, and the `truth_moment` semantics need extension.

**Schema versioning.** This guide's schemas are v0. Their evolution (new fields, new semantics) needs the same compatibility discipline as any IR — which suggests the framework itself needs a formal spec and a conformance suite.

---

## 9. Conclusion

For twenty years, the world's best product companies solved the path from vision to code with brilliant, disconnected artifacts, stitched together by senior people's judgment. Generative AI has made that arrangement simultaneously obsolete and, for the first time, formalizable: obsolete because the automated endpoints expose the artisanal middle as the bottleneck; formalizable because the cost of producing and regenerating structured artifacts has collapsed.

Working Forward proposes that product design gain what code always had — formal representation, versioning, diffs, lints, traceability — without losing what made it human: the PRFAQ's narrative, the storyboard's care, the blueprint's realism, the domain's rigor. The LLM compiles; the human decides; git remembers.

Amazon taught the world to work backwards to clarity. It's time to learn to work forward from it.

---

## Appendix A — Reference repository structure

```
product/
├── L0-vision/
│   ├── prfaq.md
│   └── vision.yaml
├── L1-journey/journey.yaml
├── L2-service/blueprint.yaml
├── L3-domain/domain.yaml
├── L4-experience/
│   ├── experience.yaml
│   ├── tokens.json
│   └── refs/                  # visual attachments (Figma exports, moodboards)
├── L5-specs/*.md
├── lints/wf-lints.yaml        # coherence-check configuration
└── agents/                    # compiler prompts, per boundary
    ├── l0-to-l1.md
    ├── l1-to-l2.md
    └── ...
```

## Appendix B — Gate checklist (summary)

- **G0 (vision):** customer named? problem with severity? hard questions addressed to layers? explicit non-goals?
- **G1 (journey):** does every moment have intent and emotion? moments of truth marked? no moment is a screen in disguise?
- **G2 (service):** every L2 hard question answered as a policy? every edge case has a resolution or accepted_risk? SLAs where they matter?
- **G3 (domain):** every event has an emitter and a consumer? invariants reference policies? context boundaries justified by real coupling?
- **G4 (experience):** every edge case covered by a state/transition? every validation has a pedigree? sad states have screens worthy of them?
- **G5 (specs):** every clause has a reference? no new scope? prioritization done?

---

*Working Forward v0.1 — a living document. Feedback, forks, and adversarial reviews are the method, not the exception.*
