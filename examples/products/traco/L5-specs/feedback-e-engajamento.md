# Spec: Feedback técnico e engajamento
Feature servida: [MOM-03, MOM-04, MOM-06] via [FLW-PRATICA] · Contexto: [CTX-Pratica]

WHEN um post é publicado
THE SYSTEM SHALL garantir ao menos uma janela de exposição no feed de descoberta de quem segue prompts similares, mesmo que o criador não tenha seguidores. [POL-COLDSTART-01]

IF um post não receber nenhuma reação em 72 horas mesmo com a exposição garantida
THEN THE SYSTEM SHALL oferecer 'pedir feedback' manual, encaminhando o post a um criador da comunidade que aceitou receber esses pedidos. [EDG-03]

WHEN uma reação em massa com padrão de bot/farm de engajamento é detectada
THE SYSTEM SHALL filtrar essas reações do contador público silenciosamente, sem notificar o autor da suspeita. [EDG-04]

WHEN um comentário é marcado como feedback técnico
THE SYSTEM SHALL contá-lo na métrica de retorno de qualidade do criador — reação isolada (like) nunca conta para essa métrica. [POL-FEEDBACK-01] [TEN-01]

IF o autor do post contestar a marcação de 'feedback técnico' de um comentário
THEN THE SYSTEM SHALL remover o peso de reputação desse comentarista após três contestações de autores diferentes. [EDG-10]

IF dois comentários marcados como feedback técnico conflitarem entre si na mesma obra
THEN THE SYSTEM SHALL exibir ambos lado a lado, ordenados por quantos 'isso me ajudou' o autor do post marcar, sem arbitrar qual está tecnicamente certo. [EDG-13] [FAQ-02]

---

**Nota sobre EDG-09 (não uma cláusula EARS — deliberadamente)** — o caso "criador pratica com constância mas nunca recebe reação orgânica" não tem uma cláusula THE SYSTEM SHALL correspondente nesta spec, e isso é proposital. `blueprint.yaml` registra EDG-09 sem `resolution` nem `accepted_risk` porque as duas posições em jogo (forçar feedback sintético vs. aceitar o risco de churn silencioso) nunca foram decididas — ver `NOTES.md`. RCT-04/EDG-03 cobrem apenas a metade "resolvida" (o limiar de 72h); escrever uma cláusula EARS aqui como se o debate estivesse fechado seria inventar escopo que a camada anterior não aprovou — exatamente o que o check `spec-anchoring` deste repositório existe para impedir.
