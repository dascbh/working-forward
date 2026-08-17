# Spec: Verificação de resultado e liberação de custódia
Feature servida: [MOM-02] [MOM-04] [MOM-05] via [FLW-DELEGAR] · Contexto: [CTX-Pagamento] [CTX-Confianca]

WHEN o sistema emite EVT-ResultadoEntregue
THE SYSTEM SHALL executar verificação automática do resultado contra o critério de sucesso definido em MOM-01, com amostragem por revisor independente do operador. [BCK-11] [POL-VERIF-01]

THE SYSTEM SHALL liberar o escrow somente quando a verificação automática aprovar OU o mandante confirmar manualmente — liberação por decurso de prazo silencioso é proibida. [POL-VERIF-01] [TEN-02]

IF a verificação automática e o mandante discordarem do resultado
THEN THE SYSTEM SHALL manter o escrow retido e transicionar FLW-DELEGAR para 'em_disputa'. [EDG-04]

IF o resultado cumprir apenas parte do critério de sucesso
THEN THE SYSTEM SHALL liberar o escrow proporcionalmente ao percentual verificado, retendo o restante até complemento ou disputa. [EDG-05]

WHEN um mandato é concluído com escrow liberado sem disputa
THE SYSTEM SHALL atualizar o score de reputação do operador; mandato ainda em disputa não soma nem penaliza o score. [POL-REP-01] [BCK-03]

WHEN o mandante compara operadores na vitrine
THE SYSTEM SHALL exibir reputação calculada apenas sobre mandatos com verificação concluída, com tratamento explícito para operador sem histórico. [EDG-02] [EDG-03] [FAQ-05]
