# Spec: Execução supervisionada do agente
Feature servida: [MOM-03] [MOM-10] [MOM-11] [MOM-12] via [FLW-EXECUCAO] · Contexto: [CTX-Mandato]

WHEN o agente executa uma ação com efeito externo
THE SYSTEM SHALL validá-la contra o escopo e o orçamento-teto remanescente do mandato antes da execução. [POL-TETO-01] [BCK-21]

IF a ação necessária para cumprir o critério de sucesso excede o escopo original do mandato
THEN THE SYSTEM SHALL pausar a execução e transicionar FLW-EXECUCAO para 'aguardando_resposta_extensao', sem executar a ação. [EDG-06] [POL-TETO-01] [FAQ-01]

WHILE o mandato estiver no estado 'aguardando_resposta_extensao'
THE SYSTEM SHALL manter a execução pausada até resposta explícita do mandante — silêncio nunca é interpretado como autorização. [POL-EXT-01]

IF o mandante não responder à solicitação de extensão dentro de 24 horas
THEN THE SYSTEM SHALL transicionar para 'pausado_expirado' sem incorrer custo adicional, permitindo retomada a qualquer momento. [EDG-08]

IF a extensão solicitada colidir com outro mandato ativo do mesmo mandante
THEN THE SYSTEM SHALL sinalizar o conflito antes de qualquer aprovação, exigindo reconciliação explícita entre os dois mandatos. [EDG-09] [RCT-03] [FAQ-04]

WHEN o agente fica sem resposta de uma dependência externa necessária ao próximo passo
THE SYSTEM SHALL marcar o checkpoint como bloqueado com retry programado, notificando o mandante se o bloqueio ultrapassar 1 hora. [EDG-07]

WHEN o sistema emite EVT-AcaoExecutada
THE SYSTEM SHALL registrar checkpoint verificável com evidência da ação, disponível ao mandante em tempo real via SCR-MONITOR. [BCK-22] [TEN-03] [FAQ-03]
