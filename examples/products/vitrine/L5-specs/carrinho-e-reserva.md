# Spec: Carrinho e reserva de estoque
Feature servida: [MOM-01] [MOM-02] via [FLW-COMPRAR] · Contexto: [CTX-Compra] [CTX-Estoque]

THE SYSTEM SHALL exibir um item como disponível somente se o estoque real, descontando reservas ativas, for maior que zero. [POL-ESTOQUE-01] [TEN-01]

WHEN dois compradores tentam adicionar a última unidade quase simultaneamente
THE SYSTEM SHALL reservar o item para o primeiro por tempo limitado e exibir ao segundo o tempo restante da reserva, com alternativa sugerida. [EDG-01] [FAQ-01]

THE SYSTEM SHALL impedir que a mesma unidade de estoque seja reservada duas vezes simultaneamente. [FAQ-04]

WHEN o pagamento falha depois que o estoque já foi reservado
THE SYSTEM SHALL manter a reserva pelo tempo restante da janela, permitindo nova tentativa de pagamento sem perder os dados preenchidos. [EDG-02] [POL-RETOMAR-01] [FAQ-02]

IF a janela de reserva estiver prestes a expirar durante o preenchimento do checkout
THEN THE SYSTEM SHALL avisar o comprador 1 minuto antes do fim, permitindo uma extensão caso o estoque ainda permita. [EDG-03]

WHEN o comprador submete o pagamento
THE SYSTEM SHALL exigir método de pagamento válido antes de processar. [VAL-CHECKOUT-01]
