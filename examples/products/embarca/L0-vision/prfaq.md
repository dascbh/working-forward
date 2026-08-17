# Embarca — Press Release (interno, estilo Working Backwards)

**São Paulo, SP — [data de lançamento]** — A Embarca anuncia hoje uma infraestrutura de crédito embutido que decide em tempo real, dentro do checkout de qualquer plataforma parceira — o comprador nunca sai do fluxo de compra pra saber se foi aprovado.

Plataformas de e-commerce, SaaS e marketplace perdem venda no momento exato da decisão de compra: o limite do cartão do cliente não cobre o valor, e não há alternativa de parcelamento suficiente. A solução óbvia — negociar com um banco — significa meses de homologação e, no fim, uma experiência de crédito genérica que redireciona o comprador pra fora do produto. A Embarca resolve isso como infraestrutura: a decisão de crédito acontece dentro do fluxo da plataforma parceira, responde em segundos, e toda negativa vem com um motivo compreensível — e, quando possível, uma alternativa — em vez de uma porta fechada sem explicação.

"Ninguém quer saber que existe um motor de decisão de crédito rodando por trás do botão de 'comprar parcelado'. Quer é que o botão funcione. A engenharia da confiança é nossa; o resultado, do parceiro", diz o head de produto da Embarca.

A plataforma está disponível para produtos de e-commerce, SaaS e marketplace que querem oferecer crédito ao consumidor final embutido no próprio checkout, sem construir um motor de risco do zero.

## FAQ Externa

**P: Se eu for negado, fico sabendo por quê?**
R: Sim. Toda negativa vem com motivo em linguagem simples e, quando possível, uma alternativa — como um valor menor ou prazo diferente.

**P: A plataforma onde eu compro assume algum risco se eu não pagar?**
R: Não. O risco de crédito é sempre da Embarca — a plataforma parceira nunca assume passivo de inadimplência do comprador final.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando o comprador é negado?** → respondida no blueprint (L2), como política de negativa com motivo e alternativa.

**FAQ-02: Como a Embarca decide o limite de crédito sem histórico prévio do comprador na própria base?** → respondida no blueprint (L2), como edge case com uso de dados alternativos.

**FAQ-03: Como a plataforma parceira sabe, em tempo real, que uma venda foi financiada com sucesso?** → respondida na experiência (L4), como painel de acompanhamento em tempo real.

**FAQ-04: Como o sistema evita aprovar duas linhas de crédito simultâneas para o mesmo comprador em plataformas parceiras diferentes?** → respondida no domínio (L3), como invariante do agregado de solicitação.
