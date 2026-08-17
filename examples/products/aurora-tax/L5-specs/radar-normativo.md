# Spec: Radar normativo diário
Feature servida: [MOM-10] [MOM-11] via [FLW-RADAR] · Contexto: [CTX-Monitoramento]

WHEN a ingestão diária conclui (EVT-NormaIngerida)
THE SYSTEM SHALL exibir no radar as normas novas/alteradas com impacto estimado por cliente (EVT-ImpactoClassificado). [BCK-21] [BCK-22] [MOM-10]

WHILE uma norma estiver sem classificação de impacto por mais de 24 horas
THE SYSTEM SHALL exibi-la com flag 'pendente de análise', nunca a ocultando do radar. [POL-RAD-01]

IF uma fonte oficial estiver indisponível durante a janela de ingestão
THEN THE SYSTEM SHALL reexecutar com backoff e exibir banner de cobertura parcial no radar do dia. [EDG-21]

WHEN o estagiário encaminha uma norma
THE SYSTEM SHALL exigir responsável ativo na conta (VAL-RESP-01) e notificar via CMD-NotificarResponsavel. [VAL-RESP-01] [RCT-03] [MOM-11]
