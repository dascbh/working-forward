# Spec: Integração em tempo real e repasse
Feature servida: [MOM-10] [MOM-11] via [FLW-INTEGRAR] · Contexto: [CTX-Liquidacao]

WHEN o status de uma decisão de crédito muda
THE SYSTEM SHALL notificar a plataforma parceira em tempo real — nunca só em relatório do dia seguinte. [POL-STATUS-01] [FAQ-03]

IF o webhook de notificação para a plataforma parceira falhar
THEN THE SYSTEM SHALL reentregar com backoff por até 24 horas, mantendo o status sempre consultável via painel. [EDG-05]

THE SYSTEM SHALL executar o repasse à plataforma parceira somente após a decisão de crédito estar completa — nunca antes. [POL-REPASSE-01]

IF uma venda financiada for cancelada pelo comprador depois do repasse já ter sido feito
THEN THE SYSTEM SHALL estornar o valor na próxima janela de repasse, nunca cobrando retroativamente sem aviso. [EDG-06]

IF o volume de repasses num único dia exceder o processamento em lote programado
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com repasse em tempo real previsto para v2. [EDG-07]
