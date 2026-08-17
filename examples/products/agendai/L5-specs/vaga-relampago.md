# Spec: Vaga-relâmpago (lista de espera sem corrida)
Servida: [MOM-03] via [FLW-VAGA] · Contexto: [CTX-Marcacao]

WHEN uma reserva é cancelada (EVT-ReservaCancelada)
THE SYSTEM SHALL liberar o slot (CMD-LiberarSlot) e notificar a lista de espera em ondas de 1 pessoa com 30 segundos de prioridade por ordem de entrada. [RCT-01] [RCT-02] [EDG-02] [EDG-03] [FAQ-03]
