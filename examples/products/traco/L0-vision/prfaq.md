# Traço — Press Release (interno, estilo Working Backwards)

**São Paulo, SP — [data de lançamento]** — Traço anuncia hoje sua plataforma de prática diária de ilustração: um prompt novo por dia, um feed pensado para retorno técnico de verdade — não curtida vazia — e sequência de constância que nunca vira ranking de vergonha pública.

Ilustradores hobbistas e iniciantes abandonam desafios de prática diária (tipo Inktober) em poucas semanas por falta de estrutura e de retorno útil: redes sociais genéricas premiam volume, não técnica, e a maioria dos comentários recebidos não ajuda ninguém a melhorar. O Traço propõe um prompt diário como âncora, um feed que distingue reação de feedback técnico, e uma forma de recrutadores de arte descobrirem talento emergente por estilo — sem transformar o espaço de prática em vitrine de venda.

"O produto não promete que todo post vai bombar. Promete que toda prática constante, mesmo sem plateia, deixa rastro — e que quando alguém der retorno, vai ser retorno que serve", diz a fundadora.

O produto é gratuito para criadores, com um plano pago para recrutadores que buscam talento por filtro de técnica/estilo.

## FAQ Externa

**P: Se ninguém reagir ao meu desenho, eu "perco" a sequência?**
R: Não. A sequência mede se você praticou, não se alguém reagiu. Postar dentro da janela do prompt do dia conta, ponto.

**P: Quem vê que minha sequência quebrou?**
R: Só você. O Traço nunca expõe publicamente hiato ou perda de sequência — constância real tem pausa.

## FAQ Interna (hard questions)

**FAQ-01: O que conta como o momento em que ganhamos ou perdemos o criador — o post, a primeira reação, ou o padrão ao longo de semanas?** → endereçada à jornada (L1); nota honesta: o framework não tem um jeito limpo de responder isso, porque `truth_moment` é um booleano por momento discreto, e a resposta real é "depende da janela de tempo", que não é um momento. Ver `L1-journey/journey.yaml` e `NOTES.md`.

**FAQ-02: Quando dois comentaristas dão feedback técnico conflitante na mesma obra, o que o produto faz?** → respondida no blueprint (L2).

**FAQ-03: Quem é dono do número de reputação/sequência exibido no perfil — o contexto de prática que gera o evento, ou o contexto de reputação que exibe?** → é exatamente a pergunta que o domínio (L3) NÃO consegue responder de forma limpa. Ver `L3-domain/domain.yaml` (relationship de CTX-Reputacao) e `NOTES.md` — é um debate real, em aberto, sem posição vencedora.

**FAQ-04: Quando um criador apaga um post que já tinha reações, a sequência e a reputação recalculam retroativamente?** → respondida no blueprint (L2).

**FAQ-05: Como o caçador de talento contata um criador sem que o produto vire canal de spam de recrutamento dentro do feed de prática?** → respondida na experiência (L4), via opt-in explícito.
