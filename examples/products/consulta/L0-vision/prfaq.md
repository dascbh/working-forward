# Consulta — Press Release (interno, estilo Working Backwards)

**Belo Horizonte, MG — [data de lançamento]** — A Consulta anuncia hoje uma plataforma de telemedicina com triagem antes do agendamento e histórico clínico organizado na tela do médico desde o primeiro segundo — e escalação que segue o paciente quando o caso muda de mãos.

Pacientes com sintomas que poderiam ser resolvidos remotamente enfrentam a mesma fila de agendamento presencial, atrasando o cuidado. E quando finalmente entram na consulta, o médico muitas vezes não tem o histórico clínico organizado à mão, e gasta minutos preciosos da consulta reconstruindo o que já foi dito antes. A Consulta resolve as duas pontas: toda consulta passa por triagem de risco antes de ser agendada — e sintoma de possível emergência nunca entra na fila de telemedicina, é redirecionado na hora — e todo repasse de caso entre médicos leva o histórico clínico completo, para o paciente nunca contar a própria história do zero.

"Telemedicina boa não é vídeo bonito. É saber, antes de apertar o botão de atender, exatamente quem é aquele paciente e o que já foi conversado — e saber, sem sombra de dúvida, quando aquele caso não deveria estar numa chamada de vídeo", diz a diretora médica da Consulta.

A plataforma está disponível para clínicas e redes de saúde que já oferecem atendimento presencial e querem absorver consultas de baixa e média complexidade remotamente, com segurança clínica e regulatória.

## FAQ Externa

**P: Vocês atendem qualquer sintoma por vídeo?**
R: Não. Todo sintoma passa por triagem de risco antes do agendamento. Sinais de possível emergência são redirecionados imediatamente para atendimento presencial — nunca entram na fila de telemedicina.

**P: Preciso repetir meu histórico se for encaminhado a outro médico?**
R: Não. Todo repasse entre médicos leva o histórico clínico completo e uma nota de contexto do médico anterior.

## FAQ Interna (hard questions)

**FAQ-01: O que acontece quando o sintoma relatado na triagem indica possível emergência?** → respondida no blueprint (L2), como edge case com redirecionamento imediato e bloqueante.

**FAQ-02: Como o consentimento é obtido e registrado antes da consulta?** → respondida no blueprint (L2), como política de consentimento explícito obrigatório.

**FAQ-03: E se a chamada de vídeo cair no meio da consulta?** → respondida na experiência (L4), como estado de reconexão com alternativa de voz ou reagendamento.

**FAQ-04: Como o histórico clínico é transferido quando o médico repassa o caso para outro especialista?** → respondida no domínio (L3), como invariante do agregado de histórico clínico.
