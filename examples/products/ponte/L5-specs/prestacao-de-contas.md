# Spec: Prestação de contas ao financiador
Feature servida: [MOM-20] [MOM-21] via [FLW-AUDITAR] · Contexto: [CTX-PrestacaoContas]

WHEN qualquer decisão de alocação é tomada — automática ou com override
THE SYSTEM SHALL registrá-la de forma imutável e torná-la visível ao financiador em tempo real. [POL-AUDIT-01] [PROB-02]

WHEN o sistema emite EVT-TrilhaAuditoriaAtualizada
THE SYSTEM SHALL atualizar o painel do financiador sem exigir atualização manual da página. [MOM-20]

WHEN o financiador abre o detalhe de uma decisão
THE SYSTEM SHALL exibir o score de criticidade no momento, a unidade despachada, e o override com justificativa quando houver. [MOM-21]

IF o financiador questionar uma decisão de override tomada sem justificativa detalhada no momento
THEN THE SYSTEM SHALL permitir complementação retroativa, exibindo o timestamp da complementação separado do timestamp da decisão original. [EDG-08]

IF o volume de decisões durante um pico de crise exceder a capacidade de revisão manual do financiador
THEN THE SYSTEM SHALL registrar o risco como aceito para o MVP, com painel de amostragem por criticidade previsto para v2. [EDG-09]
