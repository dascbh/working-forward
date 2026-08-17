> 🇧🇷 Versão original em português: [`README.md`](README.md)

# Working Forward

**A Product Engineering framework for the age of agents — from vision to code, through formal layers.**

Amazon taught the world to work *backwards* to the vision (Working Backwards). This framework defines how to work *forward* from it: vision → journey → service → domain → experience → specification → code, with each layer as a **versionable artifact**, readable by humans and AI agents alike, with end-to-end traceability.

> Generative AI solved both ends (idea→narrative and spec→code, via SDD).
> Working Forward formalizes the middle: **product design as intermediate representation (IR)**.

📄 **[Full Reference Guide →](docs/reference-guide.en.md)**

## The layers

```
L0  VISION        prfaq.md + vision.yaml        (Amazon — Working Backwards)
L1  JOURNEY       journey.yaml                  (Airbnb — storyboarding)
L2  SERVICE       blueprint.yaml                (service blueprint — Shostack, 1984)
L3  DOMAIN        domain.yaml                   (DDD — EventStorming)
L4  EXPERIENCE    experience.yaml + tokens.json (design systems + statecharts)
L5  SPECIFICATION specs/*.md                    (EARS, derived from the layers above)
L6  ARCHITECTURE  → SDD handoff                 (Spec Kit, Kiro, BMAD, fde-kernel)
```

Principles: every layer is a contract · traceability by IDs · **the LLM compiles, the human decides** · regeneration with diff · cross-layer lints · bidirectional pipeline · native handoff to the SDD ecosystem.

## Repository structure

```
docs/reference-guide.md      The paper — read first (English: docs/reference-guide.en.md)
schemas/                     JSON Schema for each artifact (structural validation)
tools/wf_lint.py             Cross-layer coherence linter (semantic validation)
skills/                      Skills for AI clients (Claude, etc.) — one per layer
examples/artifacts/          Minimal, annotated examples, per layer
examples/products/           Full pseudo-products, L0→L5 (Portuguese)
  ├── aurora-tax/            B2B — tax intelligence platform (English mirror: examples/products-en/aurora-tax/)
  ├── agendai/                B2C — booking for barbershops
  ├── ponte/                  critical infrastructure — real-time crisis-response coordination
  ├── atende/                 AI — support chatbot with human escalation
  ├── vitrine/                e-commerce — online store with checkout and stock reservation
  ├── recorde/                SaaS — recurring billing with proration and subscription pause
  ├── consulta/                healthtech — telemedicine with triage and clinical handoff
  └── embarca/                 embedded fintech — real-time credit at a third party's checkout
examples/products-en/        English mirror of the flagship example
  └── aurora-tax/             full English translation of the aurora-tax pseudo-product, L0→L5
```

## Quickstart

**1. Validate an example product:**

```bash
pip install pyyaml jsonschema
python tools/wf_lint.py examples/products-en/aurora-tax
```

**2. Start a new product with AI:**

Add the skills from `skills/` to your AI client (in Claude: Settings → Capabilities → Skills, or via `/mnt/skills/user` in Claude Code). Then:

> "I have a product idea, I want to run Working Forward"

The `wf-orchestrator` skill detects the stage and drives the process — from the initial interview (L0) to the SDD handoff (L6), layer by layer, with explicit review gates.

**3. Structure of a product:**

```
my-product/
├── L0-vision/     prfaq.md + vision.yaml
├── L1-journey/    journey.yaml
├── L2-service/    blueprint.yaml
├── L3-domain/     domain.yaml
├── L4-experience/ experience.yaml + tokens.json
└── L5-specs/      *.md
```

## The linter

`wf_lint.py` implements the framework's "immune system" — mechanical checks for coherence across layers:

| Check | Rule |
|---|---|
| `refs-resolve` | every cross-reference points to an ID that exists |
| `hard-questions` | every hard question from L0 was consumed by its owner layer |
| `edge-coverage` | every edge case from L2 becomes a state/transition in L4, or is an `accepted_risk` |
| `event-closure` | every event in L3 has an emitter and a consumer |
| `validation-pedigree` | every validation in L4 derives from a policy or edge case |
| `spec-anchoring` | every clause in L5 references ≥1 ID from a previous layer |
| `non-goals` | no flow serves a non-goal from L0 |

## Status

**v0.1 — working draft.** Schemas and skills are living proposals; feedback, forks, and adversarial reviews are the method, not the exception. See [CONTRIBUTING.en.md](CONTRIBUTING.en.md).

## License

MIT
