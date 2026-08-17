# Spec: Triagem de risco e redirecionamento de emergência
Feature servida: [MOM-01] [MOM-20] via [FLW-CONSULTAR] · Contexto: [CTX-Triagem]

WHEN o paciente relata um sintoma
THE SYSTEM SHALL classificar o risco antes de permitir qualquer agendamento. [POL-TRIAGEM-01] [VAL-SINTOMA-01]

IF o sintoma indicar possível emergência
THEN THE SYSTEM SHALL redirecionar o paciente imediatamente para orientação de atendimento presencial, bloqueando o agendamento por vídeo. [EDG-01] [FAQ-01] [NG-01]

IF a classificação de risco pelo protocolo automático for incerta
THEN THE SYSTEM SHALL escalar o caso para triagem por enfermeiro humano antes de liberar o agendamento. [EDG-02]

IF o paciente insistir em prosseguir com consulta por vídeo após o alerta de emergência
THEN THE SYSTEM SHALL manter o bloqueio — não existe caminho de continuar mesmo assim para sintoma de emergência. [EDG-06]

IF o volume de redirecionamentos de emergência num período for atípico
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com alerta automático de anomalia previsto para v2. [EDG-07]
