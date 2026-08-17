# Ponte — Press Release (interno, estilo Working Backwards)

**Porto Alegre, RS — [data de lançamento]** — A Ponte anuncia hoje a primeira plataforma de coordenação de resposta a crises em tempo real que funciona mesmo quando a rede não funciona: necessidades verificadas no campo são triadas por criticidade, roteadas para a unidade de resposta certa, e cada decisão de alocação fica registrada e auditável — desde o primeiro relato até a prestação de contas ao financiador.

Hoje, coordenadores de campo alocam recursos escassos — água, remédio, resgate — com planilha, rádio e WhatsApp, sem visão unificada de onde a necessidade é mais crítica. O resultado é previsível: uma zona recebe recurso duplicado enquanto outra fica sem nenhum, e ninguém decide isso de má vontade — decide às cegas. A Ponte substitui a cegueira por um pipeline: necessidade reportada (mesmo offline) → verificação sem atraso do socorro → triagem por criticidade explícita, nunca por ordem de chegada → despacho da unidade certa, sem duplicidade → trilha de decisão auditável em tempo real, não em relatório pós-fato.

"A pergunta que toda operação de crise enfrenta é a mesma: por que o recurso foi para lá e não para cá? Antes da Ponte, a resposta vivia na memória de quem decidiu sob pressão. Agora ela vive no sistema, registrada no momento da decisão", diz a coordenadora de operações que ajudou a desenhar o produto.

A plataforma está disponível para organizações de resposta a desastres — defesa civil, ONGs humanitárias, agências multilaterais — operando em conjunto durante uma mesma crise, com acesso de auditoria em tempo real para financiadores e agências parceiras.

## FAQ Externa

**P: E se a internet cair no meio de uma entrega?**
R: A operação nunca é cancelada por falta de sinal. O status muda para "aguardando sincronização", com o último status confirmado sempre visível; quando a conexão volta, tudo sincroniza com o horário real dos eventos, não o horário da reconexão.

**P: Quem decide qual necessidade é atendida primeiro?**
R: Um score de criticidade explícito — urgência, vulnerabilidade e tempo em fila — nunca ordem de chegada. Qualquer decisão humana que sobreponha o score (override) exige justificativa registrada e fica visível na auditoria.

**P: O financiador só sabe onde o dinheiro foi depois que a crise acaba?**
R: Não. Cada decisão de alocação — automática ou com override — fica visível ao financiador em tempo real, com a trilha completa: score no momento, unidade despachada, justificativa quando houver.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando duas zonas pedem o mesmo recurso escasso ao mesmo tempo?** → respondida no blueprint (L2), como edge case com priorização por score e fila automática para a zona não atendida.

**FAQ-02: Como verificar uma necessidade reportada sem atrasar o socorro?** → respondida no blueprint (L2), como edge case com triagem provisória por urgência declarada enquanto a verificação completa não chega.

**FAQ-03: E se o campo perder conectividade no meio da operação?** → respondida na experiência (L4), como estado degradado que nunca cancela a alocação em andamento.

**FAQ-04: Como o sistema evita que a mesma unidade de resposta seja despachada para dois pedidos ao mesmo tempo?** → respondida no domínio (L3), como invariante estrutural do agregado de unidade.

**FAQ-05: Quem decide a prioridade quando o critério técnico de triagem e o pedido político ou de imprensa entram em conflito?** → respondida no blueprint (L2), como edge case com override permitido, mas nunca automático nem invisível.
