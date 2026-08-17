# Spec: Resposta do bot e limiar de confiança
Feature servida: [MOM-02] via [FLW-CONVERSAR] · Contexto: [CTX-Atendimento]

WHEN o bot gera uma resposta
THE SYSTEM SHALL calcular seu score de confiança antes de exibi-la ao cliente. [BCK-02] [POL-CONF-01]

IF a resposta não puder citar uma fonte correspondente na base de conhecimento
THEN THE SYSTEM SHALL bloquear sua exibição e oferecer escalação em vez de arriscar uma resposta não fundamentada. [EDG-01] [FAQ-02]

IF a pergunta estiver fora do escopo da base de conhecimento
THEN THE SYSTEM SHALL reconhecer o limite e oferecer escalação direta, sem tentar responder por aproximação. [EDG-02]

WHEN uma resposta é bloqueada por baixa confiança
THE SYSTEM SHALL sinalizar o tema para revisão da base de conhecimento. [RCT-03] [POL-REVISAO-01]
