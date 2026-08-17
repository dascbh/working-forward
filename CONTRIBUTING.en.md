> 🇧🇷 Versão original em português: [`CONTRIBUTING.md`](CONTRIBUTING.md)

# Contributing

Working Forward is a framework at v0.1 — the goal of this phase is to validate the layers, the schemas, and the skills against real products.

**Ways to contribute, in order of value:**

1. **Run the framework on a real product** (or a pseudo-product) and open a PR with the result in `examples/products/`. Every new product stresses the schemas in a different way.
2. **Adversarial review of the schemas** — find the product that does NOT fit the current schemas and document why (issue with the `schema-gap` label).
3. **Improve the skills** — the skills in `skills/` are the compilers between layers. Transcripts of real sessions (anonymized) showing where a skill drove badly are gold.
4. **New lints** — cross-layer coherence rules that catch real incoherence.
5. **L6 adapters** — handoffs to specific SDD frameworks (Spec Kit, Kiro, BMAD, OpenSpec).

**Conventions:**
- IDs follow the `PREFIX-NAME` pattern (e.g. `POL-CIT-01`, `MOM-03`). Prefixes by type are defined in the schemas.
- Artifacts in YAML, specs in Markdown with inline `[ID]` references.
- Example PRs must pass `python tools/wf_lint.py <product>` clean (or declare `accepted_risk`).
- Language: PT-BR is the primary language for new content; core docs and one flagship example are also available in English (README.en.md, CONTRIBUTING.en.md, docs/reference-guide.en.md, examples/products-en/aurora-tax/).
