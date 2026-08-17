# Spec: Confirmação de pedido
Feature servida: [MOM-03] via [FLW-COMPRAR] · Contexto: [CTX-Compra]

THE SYSTEM SHALL confirmar um pedido somente após o pagamento ser aprovado — nunca por reserva de estoque isolada. [POL-CONFIRMA-01]

WHEN o sistema emite EVT-PagamentoAprovado
THE SYSTEM SHALL dar baixa definitiva no estoque reservado e emitir o pedido. [RCT-01] [BCK-04]

IF o método de pagamento for assíncrono (ex: PIX ou boleto)
THEN THE SYSTEM SHALL manter o pedido como 'aguardando pagamento' com o estoque reservado até o prazo do método, confirmando assim que o pagamento compensar. [EDG-04]
