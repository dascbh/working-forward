# Spec: Proração e troca de plano
Feature servida: [MOM-01] [MOM-02] [MOM-03] via [FLW-ASSINAR] · Contexto: [CTX-Assinatura] [CTX-Faturamento]

WHEN o assinante confirma uma troca de plano no meio do ciclo
THE SYSTEM SHALL calcular e exibir a proração — valor creditado do plano antigo, valor cobrado do novo — antes de qualquer cobrança. [POL-PRORACAO-01] [TEN-01]

IF o assinante trocar de plano mais de uma vez no mesmo ciclo de cobrança
THEN THE SYSTEM SHALL calcular cada proração com base no estado anterior, refletindo a sequência completa de trocas — nunca apenas a última. [EDG-01] [FAQ-01]

THE SYSTEM SHALL impedir que o mesmo período seja cobrado duas vezes quando houver upgrade e downgrade no mesmo dia. [FAQ-04]

IF a troca envolver mudança de ciclo mensal para anual (ou o inverso)
THEN THE SYSTEM SHALL converter o valor não utilizado do ciclo atual em crédito proporcional ao novo ciclo. [EDG-02]

WHEN uma fatura é emitida
THE SYSTEM SHALL discriminar proração e cobrança por uso separadamente da mensalidade. [POL-FATURA-01] [EDG-03]
