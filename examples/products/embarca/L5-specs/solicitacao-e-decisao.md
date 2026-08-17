# Spec: Solicitação e decisão de crédito
Feature servida: [MOM-01] [MOM-02] via [FLW-DECIDIR] · Contexto: [CTX-Solicitacao] [CTX-Credito]

THE SYSTEM SHALL manter toda etapa da solicitação de crédito dentro do fluxo da plataforma parceira, sem redirecionamento externo. [POL-EMBUTIDO-01]

WHEN o comprador submete uma solicitação de crédito
THE SYSTEM SHALL exigir valor numérico maior que zero e menor ou igual ao valor da compra antes de processar. [VAL-SOLICITACAO-01]

IF o comprador já tiver uma solicitação em análise em outra plataforma parceira no mesmo momento
THEN THE SYSTEM SHALL tratar a nova solicitação em conjunto com a existente, nunca aprovando duas linhas simultâneas de forma independente. [EDG-01] [FAQ-04]

THE SYSTEM SHALL responder a decisão de crédito em tempo real dentro do checkout. [POL-DECISAO-01]

IF o comprador não tiver histórico de crédito prévio na base da Embarca
THEN THE SYSTEM SHALL usar dados alternativos em vez de negar automaticamente por falta de histórico. [EDG-02] [FAQ-02]

IF o motor de decisão exceder o tempo-alvo de resposta
THEN THE SYSTEM SHALL exibir status 'em análise' com prazo estimado e opção de finalizar a compra por outro método. [EDG-03]

WHEN o comprador é aprovado
THE SYSTEM SHALL exigir aceite explícito das condições antes de finalizar a compra financiada. [VAL-CONDICOES-01]
