# Exemplos de artefatos

- `templates/` — esqueletos mínimos comentados de cada artefato, prontos pra copiar num produto novo.
- Para exemplos **completos e consistentes entre si** (que passam no linter), veja `../products/aurora-tax` (B2B, jornadas lineares + loop, modo degradado, escalação humana), `../products/agendai` (B2C, concorrência de slots, lista de espera, replanejamento em cascata), `../products/ponte` (infraestrutura crítica, ator não-persona na jornada, 4 bounded contexts, operação offline-first, prestação de contas auditável), `../products/atende` (chatbot de IA, limiar de confiança, escalação com contexto preservado) e `../products/vitrine` (e-commerce, reserva de estoque com expiração, checkout resiliente a falha de pagamento).

Regra de ouro ao preencher: **todo campo de referência aponta pra um ID que existe** — rode `python ../../tools/wf_lint.py <seu-produto>` cedo e sempre.
