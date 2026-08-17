# Atende — Press Release (interno, estilo Working Backwards)

**Curitiba, PR — [data de lançamento]** — A Atende anuncia hoje uma plataforma de atendimento por IA que resolve o que sabe resolver bem e escala para humano no momento certo — nunca prende o cliente num loop de respostas robóticas sem saída.

Times de atendimento crescem a fila de tickets mais rápido do que conseguem contratar. A resposta óbvia — um chatbot de IA — costuma trocar um problema por outro: o bot responde com confiança mesmo quando não sabe, e o cliente frustrado gasta mais tempo tentando escapar do robô do que teria gasto esperando um humano. A Atende resolve isso assumindo o limite do bot como parte do produto, não como falha: toda resposta de baixa confiança é bloqueada antes de ser exibida, e a escalação para humano acontece com um clique — sempre com o histórico completo, para o cliente nunca ter que se repetir.

"O bot bom não é o que responde tudo. É o que sabe a hora de dizer 'deixa eu te passar para alguém que resolve isso melhor' — e faz isso sem o cliente ter que implorar", diz a líder de produto da Atende.

A plataforma está disponível para empresas de e-commerce e SaaS que já têm um time de atendimento humano e querem absorver o crescimento do volume sem crescer a fila proporcionalmente.

## FAQ Externa

**P: O bot pode inventar uma resposta errada?**
R: Toda resposta precisa citar a fonte na base de conhecimento da empresa. Sem fonte correspondente, a resposta não é exibida — o bot oferece escalação em vez de arriscar.

**P: Consigo falar com um humano quando quiser?**
R: Sim, a qualquer momento da conversa, sem barreira. E quando escala, o atendente já recebe o histórico completo — você não repete o que já disse.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando o bot não sabe responder?** → respondida no blueprint (L2), como edge case com escalação em vez de resposta arriscada.

**FAQ-02: Como o bot evita dar informação errada com confiança (alucinação)?** → respondida no blueprint (L2), como política de citação obrigatória da fonte.

**FAQ-03: E se o cliente ficar frustrado no meio da conversa?** → respondida na experiência (L4), como estado de oferta de escalação proativa.

**FAQ-04: Como o histórico da conversa é preservado quando escala para humano?** → respondida no domínio (L3), como invariante do agregado de conversa.
