# Spec: Recuperação de carrinho e gestão de estoque
Feature servida: [MOM-10] [MOM-11] [MOM-20] [MOM-21] via [FLW-RECUPERAR] [FLW-GERENCIAR] · Contexto: [CTX-Compra] [CTX-Estoque]

WHEN um carrinho é identificado como abandonado
THE SYSTEM SHALL enviar lembrete respeitando a preferência de comunicação do comprador. [POL-LEMBRETE-01]

IF um item do carrinho abandonado ficar indisponível antes do envio do lembrete
THEN THE SYSTEM SHALL exibir o item como indisponível com alternativa sugerida, nunca convidando a retomar um checkout que vai falhar. [EDG-05] [FAQ-03]

THE SYSTEM SHALL liberar automaticamente o estoque reservado ao expirar a janela sem pagamento confirmado — nunca deixando-o preso indefinidamente. [POL-LIBERA-01]

IF o lojista quiser estender manualmente a reserva de um pedido específico
THEN THE SYSTEM SHALL exigir motivo registrado antes de aplicar a extensão. [EDG-06] [VAL-EXTENSAO-01]

IF o volume de pedidos com falha de pagamento em pico de tráfego exceder a capacidade da fila de liberação
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com liberação instantânea em escala prevista para v2. [EDG-07]
