# Spec: Consentimento e realização da consulta
Feature servida: [MOM-02] [MOM-03] via [FLW-CONSULTAR] · Contexto: [CTX-Atendimento]

THE SYSTEM SHALL exigir consentimento explícito registrado antes de iniciar qualquer consulta — nunca implícito por avançar de tela. [POL-CONSENT-01] [FAQ-02]

IF o paciente for menor de idade ou dependente
THEN THE SYSTEM SHALL exigir consentimento do responsável legal, com vínculo verificado antes de liberar a consulta. [EDG-03]

WHEN uma consulta é iniciada
THE SYSTEM SHALL exibir o histórico clínico relevante ao médico antes do início da chamada — nunca montado durante a consulta. [POL-CONTEXTO-01]

IF a chamada de vídeo cair no meio da consulta
THEN THE SYSTEM SHALL tentar reconexão automática por 60 segundos preservando a sessão, oferecendo chamada de voz ou reagendamento em caso de falha. [EDG-04] [FAQ-03]
