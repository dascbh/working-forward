# Spec: Escalação para atendimento humano
Feature servida: [MOM-03] [MOM-10] via [FLW-CONVERSAR] [FLW-ATENDER] · Contexto: [CTX-Atendimento]

THE SYSTEM SHALL permitir que o cliente escale para humano a qualquer momento da conversa, sem barreira ou justificativa exigida. [POL-ESCALA-01] [FAQ-01]

IF um assunto sensível for detectado (cancelamento de conta, reclamação jurídica)
THEN THE SYSTEM SHALL escalar automaticamente, sem esperar o cliente pedir, informando o motivo. [EDG-03] [NG-01]

IF sinais de frustração forem detectados (linguagem, repetição da mesma pergunta)
THEN THE SYSTEM SHALL oferecer escalação proativa após 2 tentativas sem sucesso. [EDG-04] [FAQ-03]

IF todos os atendentes humanos estiverem ocupados no momento da escalação
THEN THE SYSTEM SHALL exibir posição na fila e tempo estimado, mantendo o bot disponível em paralelo. [EDG-05]

WHEN uma conversa é escalada
THE SYSTEM SHALL montar o resumo de contexto a partir do histórico completo antes de entregá-la ao atendente — o cliente nunca se repete. [POL-CONTEXTO-01] [TEN-02] [FAQ-04]

IF a conversa tiver mais de 50 mensagens antes da escalação
THEN THE SYSTEM SHALL gerar um resumo automático dos pontos principais com link para o transcript completo. [EDG-06]
