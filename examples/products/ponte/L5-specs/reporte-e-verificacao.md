# Spec: Reporte e verificação de necessidade
Feature servida: [MOM-01] [MOM-02] via [FLW-REPORTAR] · Contexto: [CTX-Necessidade]

WHEN o reportante envia um relato de necessidade
THE SYSTEM SHALL aceitá-lo mesmo sem conectividade, preservando o timestamp original até a sincronização. [EDG-01] [VAL-RELATO-01]

WHEN dois relatos descrevem a mesma necessidade em raio de 200m e janela de 30 minutos
THE SYSTEM SHALL agrupá-los como um único pedido, nunca como pedidos independentes. [POL-DEDUP-01]

THE SYSTEM SHALL negar uma necessidade apenas após tentativa de verificação — nunca por decurso de prazo silencioso. [POL-VERIF-01] [TEN-02]

IF não houver segundo relato nem coordenador disponível para confirmar em até 30 minutos
THEN THE SYSTEM SHALL manter a necessidade visível na triagem como 'não verificada, urgência declarada', nunca oculta. [EDG-02] [FAQ-02]

IF um relato for identificado como falso ou malicioso
THEN THE SYSTEM SHALL marcá-lo como 'invalidado' com motivo registrado, sem banir o reportante automaticamente. [EDG-03]
