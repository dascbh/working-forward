> 🇺🇸 English version available: [`CONTRIBUTING.en.md`](CONTRIBUTING.en.md)

# Contribuindo

O Working Forward é um framework em v0.1 — o objetivo desta fase é validar as camadas, os schemas e as skills contra produtos reais.

**Formas de contribuir, em ordem de valor:**

1. **Rode o framework num produto real** (ou pseudo-produto) e abra um PR com o resultado em `examples/products/`. Cada produto novo estressa os schemas de um jeito diferente.
2. **Adversarial review dos schemas** — encontre o produto que NÃO cabe nos schemas atuais e documente por quê (issue com label `schema-gap`).
3. **Melhore as skills** — as skills em `skills/` são os compiladores entre camadas. Transcripts de sessões reais (anonimizados) que mostrem onde a skill conduziu mal são ouro.
4. **Novos lints** — regras de coerência entre camadas que pegam incoerência real.
5. **Adapters L6** — handoffs para frameworks SDD específicos (Spec Kit, Kiro, BMAD, OpenSpec).

**Convenções:**
- IDs seguem o padrão `PREFIX-NOME` (ex: `POL-CIT-01`, `MOM-03`). Prefixos por tipo estão nos schemas.
- Artefatos em YAML, specs em Markdown com referências `[ID]` inline.
- PRs de exemplo devem passar `python tools/wf_lint.py <produto>` limpo (ou declarar `accepted_risk`).
- Idioma: PT-BR é o idioma primário para conteúdo novo; os docs centrais e um exemplo completo (flagship) também estão disponíveis em inglês (README.en.md, CONTRIBUTING.en.md, docs/reference-guide.en.md, examples/products-en/aurora-tax/).
