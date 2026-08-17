# Spec: Resposta fundamentada à consulta
Feature servida: [MOM-03] via [FLW-CONSULTA] · Contexto: [CTX-Consultoria]

WHEN o sistema emite EVT-ConsultaRespondida
THE SYSTEM SHALL exibir cada afirmação normativa com citação clicável verificada contra fonte primária, com selo de verificação por citação. [POL-CIT-01] [MOM-03]

WHEN a validação de citação falha (EVT-CitacaoInvalidada)
THE SYSTEM SHALL transicionar FLW-CONSULTA para o estado 'reformulando' sem exibir a resposta não verificada, informando que a reverificação está em curso. [RCT-01] [POL-CIT-01]

WHEN duas ou mais normas aplicáveis conflitam
THE SYSTEM SHALL exibir todas as normas conflitantes e o critério de resolução aplicado (hierarquia, cronologia ou especialidade). [POL-CONF-01] [FAQ-07]

WHEN a norma fundamentante foi publicada há menos de 24 horas
THE SYSTEM SHALL exibir a resposta com ressalva de vigência explícita e agendar reindexação prioritária. [EDG-05] [FAQ-11]

IF o processamento exceder 8 segundos (EVT-RespostaDegradada)
THEN THE SYSTEM SHALL exibir resposta parcial com aviso e notificar o usuário quando a resposta completa estiver disponível. [EDG-07] [BCK-11]

IF nenhum dispositivo for encontrado para fundamentar a resposta
THEN THE SYSTEM SHALL declarar a impossibilidade de fundamentar e escalar para revisão humana com prazo exibido. [EDG-08] [RCT-02]
