# Spec: Pausa e retomada de assinatura
Feature servida: [MOM-10] [MOM-11] via [FLW-PAUSAR] · Contexto: [CTX-Assinatura]

WHEN o assinante pausa a assinatura
THE SYSTEM SHALL preservar configurações, histórico e integrações da conta — o cliente não perde nada além do acesso durante o período. [POL-PAUSA-01] [FAQ-03]

IF o assinante pausar no meio de um ciclo já pago
THEN THE SYSTEM SHALL manter o ciclo ativo até o fim antes de suspender a cobrança, sem reembolso automático. [EDG-04]

WHEN o assinante define a duração da pausa
THE SYSTEM SHALL exigir que a duração esteja dentro do limite máximo permitido. [VAL-PAUSA-01]

IF o período máximo de pausa expirar sem o assinante retomar
THEN THE SYSTEM SHALL manter a conta pausada com aviso recorrente, nunca cancelando automaticamente sem novo aviso explícito. [EDG-05]
