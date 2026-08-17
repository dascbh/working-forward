# NOTES — Traço como anti-template

Este produto não existe para ser um nono exemplo bonito. Ele existe para testar
os pontos que o `docs/reference-guide.md`, seção 8 ("Limitações e questões
abertas"), admite não saber resolver — especialmente **"produtos
não-transacionais"** e a tensão permanente entre formalidade e expressividade.
Os outros 8 exemplos deste repositório (aurora-tax, ponte, agendai, atende,
consulta, embarca, recorde, vitrine) são todos, no fundo, produtos
transacionais com jornadas de começo-meio-fim, mesmo quando têm um `shape:
loop` — a jornada em loop de `ponte` (coordenação de crise) ainda tem um
`truth_moment` claro e único por momento, e toda `relationship` de bounded
context nos 8 exemplos é uma linha só, sem debate. Traço tenta genuinamente
não caber nesse molde, porque um feed de prática criativa contínua não cabe.

Resultado do lint no final deste documento. Aqui vai o porquê de cada
friç­ão, na ordem em que apareceria numa revisão de camada.

---

## 1. `truth_moment` num produto de loop não tem resposta limpa (L1)

`journey.yaml` marca `truth_moment: true` em **quatro** momentos da mesma
jornada (MOM-02, MOM-03, MOM-04, MOM-07). Isso não é indecisão nossa — é a
tradução mais honesta possível de uma pergunta real (FAQ-01) que a visão
formalmente delega para L1 e que L1 não tem vocabulário para responder:

> "O que conta como o momento em que ganhamos ou perdemos o criador — o post,
> a primeira reação, ou o padrão ao longo de semanas?"

A resposta real do produto é: **nenhum desses momentos, isoladamente, decide
nada.** O que decide é o padrão agregado sobre uma janela de várias semanas —
se o criador teve constância suficiente e retorno suficiente para não
desistir. Isso é uma propriedade estatística sobre uma sequência de eventos,
não um evento. O schema de `journey.yaml`
(`schemas/journey.schema.json`) define `truth_moment` como um booleano por
`moment` discreto. Não existe (e não deveria existir só pra este produto, de
forma improvisada) um jeito de expressar "truth moment sobre uma janela
deslizante de N ocorrências do loop" sem inventar uma extensão de schema que
nenhum outro produto usaria e que não foi revisada por ninguém.

**O que fizemos:** marcamos os quatro candidatos como `true`, com comentário
inline em cada um explicando por que ele é candidato e por que não é
suficiente sozinho — e documentamos aqui, explicitamente, que isso é uma
tradução com perda, não uma resposta.

**O que uma extensão de schema plausível faria** (não implementada — é
proposta, não fato deste produto): um `truth_moment` deixaria de ser só
`boolean` e passaria a aceitar algo como
`{ type: aggregate, window: "4 semanas", of: [MOM-02, MOM-03, MOM-04, MOM-07] }`
— um momento de verdade *sintético*, calculado sobre outros momentos, em vez
de um momento vivido. Isso teria consequências em L2 (que política mede a
janela?) e em L4 (que estado de UI representa "quatro semanas boas", já que
não é uma tela?). Não resolvemos isso aqui de propósito — é exatamente o tipo
de mudança de schema que merece revisão própria, não um hack de exemplo.

---

## 2. A fronteira de contexto contestada: CTX-Pratica × CTX-Reputacao (L3)

Este é o ponto que o enunciado deste exercício pediu explicitamente: uma
relação de bounded context que dois engenheiros sêniores razoáveis
discordariam de verdade, documentada com prós/contras reais, sem resolução
artificial.

**A pergunta (FAQ-03):** quem é dono do número de reputação/sequência exibido
no perfil — o contexto que gera o evento (CTX-Pratica, quando alguém reage ou
comenta) ou o contexto que exibe o número (CTX-Reputacao)?

**Posição A — shared-kernel de fato, escrita síncrona.**
`CMD-PublicarPost` e `CMD-ReagirPost` escrevem diretamente nos contadores de
`AGG-Perfil` na mesma transação em que registram o post/reação.
- Prós: MOM-03 ("esperar a primeira reação") e MOM-05 ("ver a sequência")
  ficam com atualização instantânea — que é literalmente a emoção-alvo desses
  momentos (ansiedade → alívio, orgulho). Um atraso de fila aqui mata
  exatamente o que o produto tenta entregar.
- Contras: dois contextos passam a co-possuir os invariantes de `AGG-Perfil`,
  o que acopla deploy de `CTX-Pratica` e `CTX-Reputacao` — o tipo de escrita
  cruzada de fronteira que o DDD clássico trata como cheiro de arquitetura. E
  o caso EDG-14 (post apagado que já tinha reações) exige uma escrita
  compensatória que, em serviços separados, precisa de coordenação
  distribuída pra não divergir.

**Posição B — customer-supplier / downstream-conformist, assíncrono.**
`CTX-Reputacao` assina os eventos de `CTX-Pratica`
(`EVT-PostPublicado`, `EVT-ReacaoRegistrada`, `EVT-ComentarioTecnicoRegistrado`)
e recalcula sua própria projeção, eventualmente consistente.
- Prós: fronteiras limpas, é o padrão usado em **todos** os outros 8 produtos
  deste repositório, e `TEN-03` (reputação reconstruível a partir do log de
  eventos) sai de graça.
- Contras: introduz atraso perceptível — segundos a minutos, dependendo da
  fila — exatamente no momento em que a jornada mais precisa de resposta
  imediata. Um "curtiu, mas você só vai saber daqui a um minuto" é uma
  degradação real da experiência que o produto promete resolver.

**Status:** sem resolução. `domain.yaml` registra
`type: "contestado (FAQ-03) — ... sem decisão"` em vez de forçar um dos
rótulos limpos (`shared-kernel`, `customer-supplier`,
`downstream-conformist`, `upstream-published-language`) que os outros 8
exemplos usam sempre em uma linha, sem debate. O campo `type` do schema é uma
string livre — isso permitiu registrar o impasse sem quebrar o schema, mas é
uma decisão de arquitetura real que ficou sem dono. Numa revisão de verdade
(o gate L2→L3, que o reference guide chama de "a revisão mais cara do
pipeline"), isso teria que ser resolvido por quem vai arcar com o custo de
reversão — não por um exemplo de repositório.

---

## 3. Um edge case deixado deliberadamente fora do schema (L2 — `EDG-09`)

`blueprint.yaml`, dentro de `MOM-03`, tem um item `EDG-09` sem `resolution`
nem `accepted_risk`. O schema (`blueprint.schema.json`) exige um dos dois via
`anyOf` — e isso **falha a validação de schema de propósito**. Não é um erro
de preenchimento; é a mesma questão em aberto da seção 2, mas na camada de
regra de negócio em vez de arquitetura:

> Um criador pratica com constância mas nunca recebe reação orgânica por
> semanas. O produto deveria forçar feedback sintético (fila de "pedir
> comentário") ou aceitar o risco de churn silencioso e deixar o feedback
> ser só o que é autêntico?

Isso **não é** um `accepted_risk` — `accepted_risk` no schema exige `owner` e
`date`, isto é, alguém assumindo a decisão de não agir. Aqui ninguém decidiu
nada, nem mesmo "vamos aceitar o risco por enquanto": as duas posições têm
argumento de peso (uma protege `TEN-01`, a outra protege `PROB-01`) e nenhuma
foi testada. Forçar isso para `accepted_risk` com um `owner` fictício seria
inventar uma decisão que não existe, só para o exemplo "fechar limpo" — o
oposto do que este exercício pediu.

`RCT-04`/`EDG-03` (72h sem reação → oferecer feedback manual) implementam uma
versão fraca da Posição A como comportamento default de produção — porque um
produto real precisa de *algum* comportamento, mesmo com o debate em aberto.
Isso está anotado em `domain.yaml` e `blueprint.yaml`: a existência de
`RCT-04` não significa que a pergunta de fundo foi respondida.

**Resultado esperado do lint:** o check `schemas` (nível `commit`) falha
nesse único ponto. Isso é o objetivo deste produto, não um bug.

---

## 4. O formalismo de statechart pressupõe transições determinísticas (L4)

`experience.yaml`, estado `aguardando_engajamento` de `FLW-PRATICA`, tem um
comentário longo sobre isto: toda outra transição de saída "de espera" neste
repositório é disparada por um evento determinístico de sistema — um SLA
técnico real (`TIMEOUT_8S` em aurora-tax é o tempo de um pipeline de RAG que
alguém mediu). Aqui, a transição normal de saída depende da vontade
assíncrona de outro ser humano reagir ou comentar — sem prazo real.
`EVT-PostSemReacao72h` existe só para dar ao estado uma saída garantida, mas
72h é um **limiar de produto** (quanto é aceitável esperar antes de
intervir), não um SLA técnico medido. Modelar "esperar atenção humana" com o
mesmo formalismo que modela "esperar um serviço responder" é a costura
visível entre um formalismo bom para sistemas e a realidade de um produto
social. Não inventamos um formalismo novo pra consertar isso — documentamos a
costura.

Relacionado: o estado `sem_engajamento` cobre `EDG-09`, mas só consegue
representar a Posição A do debate (oferecer feedback manual). A Posição B
("não fazer nada") não tem estado correspondente, porque "não fazer nada" não
é uma tela — é a ausência de uma. Um statechart exige uma transição concreta
para algum estado nomeado; não tem como representar "a opção vencedora ainda
não foi escolhida" como um estado de primeira classe.

---

## 5. Onde a assimetria entre jornadas foi deixada de propósito

`JRN-PRATICAR` (loop) tem 7 momentos, ~14 edge cases e a maior parte do
iceberg do produto. `JRN-DESCOBRIR` (linear) tem 2 momentos e praticamente
nenhum edge case (`MOM-10` não tem `policies`/`edge_cases` no blueprint;
`MOM-11` tem `backstage: []` proposital). Isso não foi suavizado para as duas
jornadas "parecerem do mesmo tamanho" como acontece, por simetria de
composição, nos 8 exemplos existentes — porque o domínio real não é
simétrico: quase todo o valor e quase todo o risco do produto está no loop de
prática, e a descoberta de talento é, de fato, uma jornada transacional
simples anexada ao mesmo produto.

---

## Resultado do lint (rodado ao final da construção)

```
$ python3 tools/wf_lint.py examples/products/traco

Working Forward lint — traco
camadas presentes: vision, journey, blueprint, domain, experience; specs: 3

✖ [commit  ] schemas
      - blueprint.yaml @ blueprints/1/edge_cases/2: EDG-09 ... is not valid under any of the given schemas
✔ [commit  ] refs-resolve       — 100 IDs declarados, todas as referências resolvem
✔ [advisory] hard-questions     — toda hard question foi consumida pela camada dona
✔ [commit  ] edge-coverage      — todo edge case coberto (covers) no L4 ou aceito com dono
✔ [advisory] event-closure      — todo evento tem emissor e consumidor
✔ [commit  ] validation-pedigree — toda validação tem pedigree em POL-*/EDG-*
✔ [commit  ] spec-anchoring     — toda cláusula EARS ancorada em ≥1 ID
✔ [advisory] non-goals          — todo NG-* citado fora do L0 em contexto de recusa/bloqueio confirmado

resultado: FALHOU
```

A única falha é o `schemas` check, no único ponto (`EDG-09`) descrito na
seção 3 acima. Todo o resto do produto — referências, cobertura de edge
cases, fechamento de eventos, pedigree de validação, ancoragem de specs e
respeito a non-goals — está limpo, incluindo a parte mais difícil (a
jornada em loop e a fronteira contestada), que passam no lint precisamente
porque documentamos a tensão em vez de escondê-la atrás de um rótulo bonito.
Um `accepted_risk` datado e assinado por um dono, ou uma `resolution` de
mentirinha, faria o lint passar 100% — e mentiria sobre o estado real da
decisão de produto. Preferimos o exemplo sujo e verdadeiro ao exemplo limpo
e falso.
