# Spec: Repasse clínico entre médicos
Feature servida: [MOM-10] [MOM-11] via [FLW-ATENDER] · Contexto: [CTX-Prontuario]

WHEN um médico repassa um caso para outro especialista
THE SYSTEM SHALL transferir o histórico clínico completo e a nota de contexto do médico de origem — o paciente nunca reconta a história do zero. [POL-REPASSE-01] [TEN-03] [FAQ-04]

IF nenhum especialista do tipo necessário estiver disponível no momento do repasse
THEN THE SYSTEM SHALL colocar o caso em fila prioritária com o histórico já anexado, informando o tempo estimado ao paciente. [EDG-05]
