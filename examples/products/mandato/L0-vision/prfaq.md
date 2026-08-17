# Mandato — Press Release (interno, estilo Working Backwards)

**São Paulo, SP — [data de lançamento]** — A Mandato anuncia hoje a primeira infraestrutura de confiança para a economia de agentes autônomos: uma plataforma onde empresas e profissionais delegam tarefas a agentes de IA com o mesmo rigor de um contrato — escopo, orçamento-teto e critério de sucesso travados antes da primeira ação — e só pagam quando o resultado é verificado, nunca quando é apenas prometido.

Hoje, delegar uma tarefa consequente a um agente autônomo significa entregar uma chave de API ou um cartão corporativo e torcer: não há registro do que o agente tem autoridade para fazer, não há garantia de que o pagamento corresponde ao que foi entregue, e não há caminho claro de responsabilização quando o agente extrapola o combinado. A Mandato resolve isso com três peças de infraestrutura, operando juntas: mandatos com escopo e orçamento-teto explícitos que o agente não pode ultrapassar sem pedir extensão; um painel de acompanhamento ao vivo que mostra cada ação relevante sem exigir vigilância constante; e um escrow que só libera o pagamento depois que o resultado é verificado contra o critério de sucesso combinado no início.

"A pergunta que todo cliente nosso fazia era a mesma: 'e se o agente fizer besteira com meu dinheiro ou meu nome?' A resposta não podia ser 'confie em nós' — tinha que ser uma trava no sistema, não uma promessa", diz a responsável por confiança e produto da Mandato.

A plataforma está disponível tanto para empresas que operam agentes de IA e querem vender essa capacidade com garantia (operadores) quanto para empresas e profissionais que precisam delegar tarefas com segurança (mandantes), em modelo de marketplace com taxa sobre o valor efetivamente liberado — nunca sobre o valor prometido.

## FAQ Externa

**P: Se o agente errar, eu perco o dinheiro?**
R: Não. O pagamento fica em custódia (escrow) até a verificação aprovar o resultado contra o critério de sucesso definido na criação do mandato. Se o resultado não bate, o valor permanece retido e o caso pode ir a arbitragem.

**P: Como o agente sabe até onde pode ir sozinho?**
R: O mandato define o escopo e o orçamento-teto antes da execução começar. Qualquer ação que exija ultrapassar esse limite pausa o agente e pede autorização explícita ao mandante — o agente nunca decide sozinho por ampliar sua própria autoridade.

**P: Quem responde se o agente causar um dano a terceiro durante a execução?**
R: A cobertura do escrow vai até o teto do mandato; operadores de agente mantêm apólice de responsabilidade obrigatória para o excedente, com o limite informado ao mandante antes da contratação.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando o agente tenta uma ação fora do escopo do mandato?** → respondida no blueprint (L2), como edge case com pausa obrigatória e pedido de extensão.

**FAQ-02: Quem é responsável — e paga — quando o agente causa dano a terceiro durante a execução?** → respondida no blueprint (L2), como edge case com cobertura de escrow + apólice do operador.

**FAQ-03: Como o mandante sabe, em tempo real, que o agente está agindo dentro do combinado, sem precisar vigiar a tela?** → respondida na experiência (L4), como painel de acompanhamento ao vivo.

**FAQ-04: E se dois mandatos do mesmo mandante pedirem ações conflitantes ao mesmo tempo?** → respondida no domínio (L3), como reconciliação explícita entre mandatos concorrentes.

**FAQ-05: Como um operador novo, sem histórico, consegue o primeiro mandato?** → respondida no blueprint (L2), como faixa "emergente" com garantia reforçada.
