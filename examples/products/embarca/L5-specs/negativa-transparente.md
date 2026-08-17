# Spec: Negativa transparente
Feature servida: [MOM-03] via [FLW-DECIDIR] · Contexto: [CTX-Credito]

WHEN o comprador é negado
THE SYSTEM SHALL exibir motivo compreensível e, quando o motivo for de valor, tentar uma alternativa de valor menor antes de negar por completo. [POL-NEGATIVA-01] [FAQ-01]

IF a negativa tiver motivo regulatório que não pode ser detalhado ao comprador
THEN THE SYSTEM SHALL exibir mensagem genérica sem alternativa e sem expor o motivo real — nunca inventando um motivo falso. [EDG-04]
