# Spec: Criação do mandato
Feature servida: [MOM-01] via [FLW-DELEGAR] · Contexto: [CTX-Mandato]

WHEN o mandante tenta publicar um mandato
THE SYSTEM SHALL exigir orçamento-teto e critério de sucesso explícitos e mensuráveis antes de aceitar a publicação. [POL-ESCOPO-01] [VAL-MANDATO-01] [NG-02]

IF a descrição da tarefa for vaga demais para gerar um critério de sucesso mensurável
THEN THE SYSTEM SHALL devolver perguntas de refinamento ao mandante e bloquear a publicação até um critério mensurável existir. [EDG-01]

WHEN o sistema emite EVT-MandatoPublicado
THE SYSTEM SHALL transicionar FLW-DELEGAR para o estado 'aguardando_operador', exibindo a vitrine de operadores. [MOM-02]
