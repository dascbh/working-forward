# Spec: Descoberta de talento
Feature servida: [MOM-10, MOM-11] via [FLW-DESCOBRIR] · Contexto: [CTX-Descoberta]

WHEN o caçador de talento busca por técnica ou estilo
THE SYSTEM SHALL retornar criadores cujo portfólio público corresponde ao filtro, incluindo disponibilidade para freelance quando ativada. [MOM-10] [BCK-20]

IF o criador não tiver ativado 'disponível para freelance' no perfil
THEN THE SYSTEM SHALL ocultar o botão de contato comercial — não existe caminho de contato fora desse opt-in. [POL-CONTATO-01] [FAQ-05]

WHEN o caçador de talento inicia contato com um criador disponível
THE SYSTEM SHALL registrar o contato e notificar o criador, e SHALL nunca misturar conteúdo comercial ao feed de prática diária — o contato fica estritamente fora dele. [EVT-ContatoComercialIniciado] [NG-01]
