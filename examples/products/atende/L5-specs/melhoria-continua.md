# Spec: Melhoria contínua da base de conhecimento
Feature servida: [MOM-20] [MOM-21] via [FLW-MELHORAR] · Contexto: [CTX-Conhecimento]

WHEN um tema acumula volume relevante de conversas de baixa confiança
THE SYSTEM SHALL sinalizá-lo para revisão do gestor, nunca descartá-lo silenciosamente. [POL-REVISAO-01] [PROB-01]

WHEN o gestor publica uma atualização na base de conhecimento
THE SYSTEM SHALL exigir citação de fonte e associação a pelo menos um tema sinalizado antes de aceitar a publicação. [VAL-BASE-01]

IF o volume de conversas de baixa confiança exceder a capacidade de revisão do gestor numa semana
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com priorização automática prevista para v2. [EDG-07]
