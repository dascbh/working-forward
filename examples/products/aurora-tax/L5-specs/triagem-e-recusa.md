# Spec: Triagem de escopo e recusa elegante
Feature servida: [MOM-01] via [FLW-CONSULTA] · Contexto: [CTX-Consultoria]

WHEN o usuário submete uma consulta
THE SYSTEM SHALL validar o texto conforme VAL-INPUT-01 antes de aceitar a submissão. [VAL-INPUT-01] [EDG-06]

IF a consulta estiver fora do escopo tributário ou solicitar peça processual
THEN THE SYSTEM SHALL recusar na entrada com motivo explícito e link para reformulação, sem registrar a consulta na fila. [POL-ESC-01] [EDG-06] [NG-01] [TEN-02]
