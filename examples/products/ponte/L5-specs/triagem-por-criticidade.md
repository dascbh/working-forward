# Spec: Triagem por criticidade
Feature servida: [MOM-10] via [FLW-COORDENAR] · Contexto: [CTX-Triagem]

WHEN uma necessidade é verificada
THE SYSTEM SHALL calcular seu score de criticidade a partir de urgência declarada, categoria e tempo em fila. [BCK-11] [POL-TRIAGEM-01]

THE SYSTEM SHALL alocar recurso escasso seguindo o score de criticidade — nunca a ordem de chegada. [TEN-01]

IF duas zonas solicitarem o mesmo recurso escasso ao mesmo tempo
THEN THE SYSTEM SHALL alocá-lo ao score de criticidade mais alto e colocar a zona não atendida em prioridade automática para o próximo recurso disponível, com ETA exibido. [EDG-04] [FAQ-01]

IF um coordenador sobrepuser o score de criticidade por pressão política ou de imprensa
THEN THE SYSTEM SHALL exigir justificativa nomeada e registrada antes de executar o override, tornando-a visível na auditoria. [EDG-05] [VAL-OVERRIDE-01] [FAQ-05]

WHEN um override é registrado
THE SYSTEM SHALL bloquear a ação caso a justificativa esteja ausente. [POL-TRIAGEM-01]
