# Spec: Marcação em tempo real
Servida: [MOM-01] [MOM-02] via [FLW-MARCAR] · Contexto: [CTX-Marcacao]

WHEN o cliente abre a vitrine
THE SYSTEM SHALL exibir apenas slots que podem ser honrados (serviço cabe antes do próximo compromisso), recalculados em ≤500ms. [POL-REAL-01] [BCK-01] [TEN-01]

WHEN dois clientes disputam o mesmo slot
THE SYSTEM SHALL confirmar o primeiro e apresentar ao segundo alternativas próximas na mesma tela, sem exigir recomeço. [EDG-01]

IF o cliente tiver 2 no-shows nos últimos 60 dias
THEN THE SYSTEM SHALL criar a reserva como pendente (EVT-ReservaPendente), exigindo confirmação até 3h antes, e devolver o slot à vitrine se não confirmada. [POL-NOSHOW-01] [FAQ-01]
