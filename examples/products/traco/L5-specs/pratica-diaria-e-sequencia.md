# Spec: Prática diária e sequência
Feature servida: [MOM-01, MOM-02, MOM-05, MOM-07] via [FLW-PRATICA] · Contexto: [CTX-Pratica, CTX-Reputacao]

WHEN o criador abre o produto no início do dia
THE SYSTEM SHALL exibir o prompt do dia com a contagem regressiva da janela de 48h para publicação vinculada ao prompt. [MOM-01] [POL-PROMPT-01]

WHEN o criador publica um post
THE SYSTEM SHALL rodar a moderação automática antes de exibir o post em qualquer feed público. [BCK-01] [POL-MOD-01]

IF a moderação automática sinalizar o post
THEN THE SYSTEM SHALL manter o post em revisão humana por até 2 horas, notificando o autor do motivo, sem descontar esse tempo da janela do prompt. [EDG-02]

WHEN um post é publicado fora da janela de 48h do prompt do dia
THE SYSTEM SHALL aceitar o post como 'fora do prompt' e não computá-lo na sequência. [POL-PROMPT-01]

WHEN a sequência do criador é recalculada após um post
THE SYSTEM SHALL usar o fuso horário declarado no perfil do criador para decidir a qual dia o post pertence. [EDG-11] [RCT-02]

IF o criador ficar 14 dias consecutivos sem postar
THEN THE SYSTEM SHALL degradar a sequência para o estado 'pausa' antes de zerá-la, nunca resetando para zero de forma visível de um só golpe. [POL-STREAK-01]

WHEN o criador apaga um post que já tinha reações ou feedback técnico contabilizados
THE SYSTEM SHALL preservar o crédito de constância já concedido — sequência e reputação NÃO recalculam retroativamente. [EDG-14] [FAQ-04]

IF o criador retomar a prática após um hiato
THEN THE SYSTEM SHALL exibir apenas o prompt de hoje, sem histórico de dias perdidos, e SHALL bloquear qualquer notificação de reengajamento (D+3, D+10, D+30) que usar linguagem de perda ou culpa. [MOM-07] [POL-RETORNO-01] [NG-03]

IF o hiato do criador exceder 90 dias
THEN THE SYSTEM SHALL preservar a sequência antiga como 'recorde pessoal' separado, exibido apenas por opção do criador, em vez de apagá-la. [EDG-12]

---

**Nota fora do escopo EARS** — esta spec não tenta responder FAQ-01 ("o que conta como o momento em que ganhamos ou perdemos o criador"). Como registrado em `L1-journey/journey.yaml` e em `NOTES.md`, a resposta honesta é que nenhum clause acima, isoladamente, é o momento de verdade — é o padrão dos quatro candidatos (MOM-02, MOM-03, MOM-04, MOM-07) ao longo de semanas. Um critério de aceite EARS por natureza descreve comportamento pontual do sistema; não existe hoje, neste framework, um jeito de escrever "THE SYSTEM SHALL, quando avaliado sobre uma janela de 4 semanas, ter sustentado retorno percebido positivo" como cláusula verificável linha a linha.
