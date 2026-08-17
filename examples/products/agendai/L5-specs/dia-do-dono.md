# Spec: O dia do dono — atraso sem drama
Servida: [MOM-11] via [FLW-DIA] · Contexto: [CTX-Operacao]

WHEN o dono registra um atraso (EVT-AtrasoRegistrado)
THE SYSTEM SHALL propor o replanejamento em cascata (EVT-CascataProposta) com nova previsão por cliente, aplicando somente após confirmação de um toque — nunca cancelando automaticamente. [POL-ATRASO-01] [RCT-03] [FAQ-02] [TEN-02]

IF a cascata estourar o expediente
THEN THE SYSTEM SHALL sugerir reagendamento com prioridade e cupom de desculpas, mantendo a decisão com o dono. [EDG-11]
