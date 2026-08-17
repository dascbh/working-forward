# Vitrine — Press Release (interno, estilo Working Backwards)

**Florianópolis, SC — [data de lançamento]** — A Vitrine anuncia hoje uma plataforma de loja virtual com checkout de um clique e estoque garantido em tempo real: o que está na vitrine é o que existe para vender, e o que o comprador preencheu no checkout nunca se perde.

Lojistas online perdem venda de duas formas silenciosas. Na entrada: checkout com fricção — login obrigatório, formulário longo — derruba conversão, e um em cada três carrinhos é abandonado no pagamento. Na saída: ruptura de estoque descoberta só depois que o pedido já foi pago, gerando cancelamento e cliente insatisfeito. A Vitrine ataca as duas pontas com a mesma disciplina: reserva de estoque em tempo real desde o carrinho, checkout que retoma de onde parou mesmo depois de uma falha de pagamento, e liberação automática de reserva quando o pagamento não se confirma — nunca deixando o item preso indefinidamente.

"O lojista não quer saber de estoque reservado, checkout resiliente ou liberação automática. Ele quer ver o pedido confirmado e o cliente satisfeito. A engenharia disso é nossa — o resultado é dele", diz a fundadora da Vitrine.

A plataforma está disponível para lojistas de médio porte (moda, casa, eletrônicos) que já vendem online e querem recuperar conversão perdida no checkout sem reescrever a loja do zero.

## FAQ Externa

**P: Se o pagamento falhar, perco os dados que já preenchi?**
R: Não. O checkout retoma exatamente de onde parou — endereço, forma de entrega e método de pagamento continuam preenchidos.

**P: Posso vender um produto que já não tenho em estoque?**
R: Não. A vitrine reflete a disponibilidade real, descontando reservas ativas de outros carrinhos — nunca um cache otimista.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando dois compradores tentam comprar a última unidade ao mesmo tempo?** → respondida no blueprint (L2), como edge case com reserva temporária e fila de espera.

**FAQ-02: E se o pagamento falhar depois que o estoque já foi reservado?** → respondida no blueprint (L2), como edge case com manutenção da reserva até o fim da janela.

**FAQ-03: Como o comprador recupera um carrinho abandonado sem perder o que já escolheu?** → respondida na experiência (L4), como fluxo dedicado de lembrete e retomada.

**FAQ-04: Como o sistema evita reservar estoque duas vezes para o mesmo item?** → respondida no domínio (L3), como invariante do agregado de estoque.
