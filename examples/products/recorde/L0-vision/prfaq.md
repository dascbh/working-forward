# Recorde — Press Release (interno, estilo Working Backwards)

**São Paulo, SP — [data de lançamento]** — A Recorde anuncia hoje uma plataforma de cobrança recorrente que acerta a proração em qualquer troca de plano e nunca transforma um pedido de pausa em cancelamento.

Toda empresa SaaS que cobra por assinatura enfrenta o mesmo ponto cego: a cobrança está certa até alguém trocar de plano no meio do ciclo — aí a proração é estimada, arredondada ou simplesmente esquecida, e o financeiro só descobre quando o cliente reclama ou quando a reconciliação do mês não fecha. E quando o cliente só quer um respiro — pausar por um tempo, não cancelar — a única opção que o produto oferece é "cancelar assinatura", perdendo um cliente que só precisava de uma pausa. A Recorde resolve os dois pontos com a mesma disciplina: toda proração é calculada e exibida antes de qualquer cobrança, e pausar é uma ação de primeira classe que preserva configurações e histórico.

"Cobrança recorrente parece simples até o segundo cliente trocar de plano no mesmo dia. A diferença entre um sistema de billing bom e um ruim mora inteira nesses casos que ninguém desenha primeiro", diz a fundadora da Recorde.

A plataforma está disponível para empresas SaaS B2B e B2C que cobram por assinatura recorrente e querem parar de corrigir fatura na mão todo fim de mês.

## FAQ Externa

**P: Se eu trocar de plano no meio do mês, quanto vou pagar?**
R: Você vê o cálculo de proração completo antes de confirmar — o que é creditado do plano antigo, o que é cobrado do novo, e a próxima data de renovação.

**P: Posso pausar minha assinatura em vez de cancelar?**
R: Sim. Pausar preserva suas configurações e histórico; você retoma exatamente de onde parou, sem reconfigurar nada.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando o cliente troca de plano duas vezes no mesmo ciclo de cobrança?** → respondida no blueprint (L2), como edge case com proração sequencial.

**FAQ-02: E se o cartão for recusado no dia da renovação?** → respondida no blueprint (L2), como edge case com janela de retentativa antes de qualquer revogação de acesso.

**FAQ-03: Como o cliente pausa a assinatura sem perder o histórico e as configurações?** → respondida na experiência (L4), como fluxo dedicado de pausa e retomada.

**FAQ-04: Como o sistema evita cobrar duas vezes pelo mesmo período quando há upgrade e downgrade no mesmo dia?** → respondida no domínio (L3), como invariante do agregado de assinatura.
