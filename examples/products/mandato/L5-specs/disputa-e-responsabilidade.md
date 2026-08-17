# Spec: Disputa e responsabilidade por dano a terceiro
Feature servida: [MOM-20] [MOM-21] via [FLW-DISPUTA] · Contexto: [CTX-Disputa]

WHEN o mandante contesta um resultado
THE SYSTEM SHALL exigir referência ao item específico do critério de sucesso não cumprido, com evidência anexada, antes de abrir a disputa. [VAL-DISPUTA-01]

WHEN o sistema emite EVT-DisputaAberta
THE SYSTEM SHALL congelar imediatamente o escrow e o score de reputação do mandato até a resolução. [BCK-31]

THE SYSTEM SHALL decidir toda disputa com base no log de execução verificável (checkpoints registrados em BCK-22), nunca apenas na palavra de uma das partes. [POL-DISP-01]

IF uma ação do agente durante o mandato causar dano a terceiro
THEN THE SYSTEM SHALL cobrir o dano com o escrow até o teto do mandato e acionar a apólice de responsabilidade obrigatória do operador para o excedente. [EDG-10] [FAQ-02]

IF o operador não responder durante o período de arbitragem
THEN THE SYSTEM SHALL resolver a disputa apenas com base no log de execução registrado, sem postergar além do prazo do painel. [EDG-11]

IF o volume de disputas simultâneas exceder a capacidade do painel de arbitragem
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com painel escalável previsto para v2. [EDG-12]
