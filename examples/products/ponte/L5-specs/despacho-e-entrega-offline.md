# Spec: Despacho e entrega sob conectividade instável
Feature servida: [MOM-11] [MOM-12] [MOM-13] via [FLW-COORDENAR] · Contexto: [CTX-Logistica]

WHEN o coordenador despacha uma unidade
THE SYSTEM SHALL confirmar sua disponibilidade antes do despacho — uma unidade não pode estar despachada para duas necessidades ao mesmo tempo. [POL-DESPACHO-01] [VAL-DESPACHO-01] [FAQ-04]

IF o despacho for bloqueado por a unidade já estar em uso em outra necessidade
THEN THE SYSTEM SHALL alertar o coordenador e notificar quando um backup estiver disponível, sem executar o segundo despacho. [RCT-05] [RCT-08]

WHILE uma unidade estiver sem conectividade durante a entrega
THE SYSTEM SHALL manter a alocação ativa — nunca cancelar ou invalidar automaticamente por perda de sinal. [POL-SYNC-01] [TEN-03]

IF a unidade ficar sem conectividade por mais de 2 horas
THEN THE SYSTEM SHALL exibir 'aguardando sincronização' com o último status confirmado e o tempo decorrido, permitindo redespacho manual de backup. [EDG-07] [FAQ-03]

WHEN a unidade aceita o despacho mas fica sem contato antes de confirmar a chegada
THE SYSTEM SHALL marcar 'em trânsito não confirmado' e alertar o coordenador após o tempo limite. [EDG-06]

WHEN a conectividade retorna
THE SYSTEM SHALL sincronizar o status da unidade preservando o timestamp original do evento, não o da reconexão. [BCK-13]
