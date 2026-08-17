# Spec: Renovação e recuperação de cobrança
Feature servida: [MOM-20] [MOM-21] via [FLW-COBRAR] · Contexto: [CTX-Cobranca]

WHEN a data de renovação de uma assinatura chega
THE SYSTEM SHALL tentar a cobrança automaticamente. [POL-RENOVA-01]

IF a cobrança de renovação falhar
THEN THE SYSTEM SHALL nunca cancelar a assinatura na primeira tentativa — entra em janela de retentativa com intervalos crescentes. [POL-RETRY-01] [FAQ-02]

WHEN o assinante atualiza o cartão durante a janela de retentativa
THE SYSTEM SHALL tentar cobrar imediatamente com o novo cartão, sem esperar a próxima data programada. [EDG-07]

IF todas as tentativas de retentativa se esgotarem sem sucesso
THEN THE SYSTEM SHALL suspender o acesso — nunca os dados — com aviso claro de como reativar. [EDG-08]

IF a assinatura mudar de moeda entre renovações
THEN THE SYSTEM SHALL usar a moeda vigente na data da cobrança, avisando o cliente antes da primeira cobrança na nova moeda. [EDG-06]
