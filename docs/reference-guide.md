> 🇺🇸 English version available: [`reference-guide.en.md`](reference-guide.en.md)

# Working Forward
## Um framework de Product Engineering para a era dos agentes — da visão ao código, por camadas formais

**Versão 0.1 — Reference Guide / Working Paper**
Agosto de 2026

---

## Resumo

A IA generativa resolveu as duas pontas do desenvolvimento de produto. Na ponta inicial, transformar uma ideia em narrativa — PRFAQ, pitch, documento de visão — tornou-se trivial. Na ponta final, transformar uma especificação em código também: o ecossistema de Spec-Driven Development (Spec Kit, Kiro, BMAD, Tessl) consolidou o loop spec → plano → tasks → implementação. O que permanece sem solução é o meio: a tradução da visão em **produto** — jornadas, fluxos, estados de tela, regras de negócio, validações, domínios e experiência — antes que qualquer especificação técnica faça sentido.

Historicamente, esse meio nunca teve um framework único. As melhores organizações de produto do mundo (Amazon, Airbnb, Uber, Netflix) resolveram fatias dele com artefatos próprios — Working Backwards e o PRFAQ, storyboarding de jornada, service blueprinting, experimentação em escala — e a comunidade de software contribuiu com o Domain-Driven Design e o EventStorming. Paralelamente, a engenharia já tinha notações formais e legíveis por máquina para pedaços desse mesmo meio — Context Mapper para fronteiras de domínio, XState/SCXML para máquinas de estado de interface, BPMN para processo, Gherkin para critério de aceite — mas cada uma isolada em ferramenta de engenheiro, nunca costurada entre si nem adotada por quem desenha produto. Em ambos os casos, cada seta entre os artefatos sempre foi uma tradução manual, com perda de informação, executada por profissionais sêniores, e nunca versionada como contrato.

**Working Forward** propõe formalizar esse pipeline completo como uma cadeia de artefatos versionáveis, legíveis por humanos e por agentes de IA, com rastreabilidade ponta a ponta e regeneração assistida por LLM entre camadas. O nome é deliberado: a Amazon nos ensinou a trabalhar *de trás pra frente* até a visão (Working Backwards); este framework define como trabalhar *pra frente* a partir dela — da visão ao código, sem que nenhuma camada intermediária viva apenas na cabeça de alguém.

---

## 1. O problema: o vale entre a visão e a spec

### 1.1 O que a era SDD resolveu — e o que ela ignora

O Spec-Driven Development estabeleceu um consenso em 2025–2026: a especificação, não o código, é a fonte da verdade. Todos os frameworks maduros convergem no mesmo loop de quatro fases — especificar, planejar, decompor em tasks, implementar — com a spec como contrato executável e regenerável.

Mas observe o que essas specs contêm: funcionalidades, critérios de aceite, restrições técnicas, casos de borda *de sistema*. Elas respondem "o que o software deve fazer". Não respondem:

- **Como o usuário atravessa o produto** — a jornada, seus momentos, suas emoções, seus pontos de abandono.
- **O que acontece nos bastidores** de cada interação — operações, integrações, processos humanos que sustentam a experiência.
- **Quais regras de negócio governam cada passo** — validações, políticas, exceções, e o que o produto faz quando elas falham.
- **Como o domínio se organiza** — quais conceitos existem, quais eventos importam, onde ficam as fronteiras entre contextos.
- **Como a experiência se materializa** — fluxos de tela, estados, transições, componentes, tokens de design.

Uma spec funcional que nasce sem essas camadas herda decisões implícitas — tomadas por ninguém, em lugar nenhum, sem registro. O agente que implementa a spec preenche os vazios com o que é estatisticamente plausível, não com o que é certo para *este* produto. O resultado é o fenômeno que qualquer time que adotou SDD reconhece: o código está correto em relação à spec, e o produto está errado em relação à intenção.

### 1.2 Por que o vale existe

O vale entre visão e spec existe porque a camada de design de produto nunca teve uma **representação formal única, compartilhada por quem desenha o produto e por quem escreve o código**. Isso não significa que a formalização nunca existiu — para domínio e experiência, em particular, ela existe há décadas, só que confinada a ferramentas de engenharia que product/design nunca adotou. Compare:

| Camada | Representação formal pré-IA | Versionável? | Legível por máquina? |
|---|---|---|---|
| Visão | PRFAQ, 6-pager | Sim (texto) | Parcialmente |
| Jornada | Storyboard, journey map | Não (imagem/board) | Não |
| Serviço | Service blueprint | Não (diagrama) | Não |
| Domínio | EventStorming (post-its!); Context Mapper/CML (DSL textual de DDD, desde ~2018) | Não (EventStorming) / Sim (CML) | Não (EventStorming) / Sim (CML) — mas de uso quase nulo fora de times de arquitetura |
| Experiência | Figma, protótipos; statecharts (Harel 1987), XState/SCXML | Proprietário (Figma) / Sim, texto (XState) | Não (Figma) / Sim (XState/SCXML) — mas como ferramenta de engenharia de front-end, fora do vocabulário de produto/design |
| Spec funcional | PRD, Gherkin, EARS | Sim | Sim |
| Código | Código | Sim | Sim |

As três camadas do meio — jornada, serviço, domínio — e a camada de experiência viviam majoritariamente em murais de post-its, boards de Miro e arquivos de Figma: artefatos ricos para humanos, opacos para máquinas, impossíveis de diffar, e desconectados entre si. Onde existia formalização real e legível por máquina — Context Mapper para domínio, XState/SCXML para experiência —, ela vivia do lado de dentro da engenharia, num vocabulário e numa ferramenta que product managers e designers nunca tocaram, isolada das camadas vizinhas. Quando a IA chegou, ela automatizou o que tinha representação formal *compartilhada entre as duas pontas* (texto nas pontas) e não tocou no que estava formalizado mas isolado, ou no que nunca foi formalizado.

### 1.3 A tese

A tese do Working Forward não é que essas camadas nunca tiveram formalismo — várias vezes tiveram. Context Mapper formaliza domínio, XState/SCXML formaliza experiência, BPMN formaliza processo, Gherkin formaliza critério de aceite. O problema nunca foi ausência de notação; foi **fragmentação**: cada formalismo nasceu isolado, dentro de uma ferramenta de engenheiro, sem referência às camadas vizinhas, e por isso nunca foi adotado por quem desenha produto.

**A tese do Working Forward é que essas camadas precisam de uma representação intermediária (IR) contínua** — não uma notação nova por camada, mas uma cadeia única, com identidades estáveis e referências cruzadas entre camadas, um conjunto de lints que verifica coerência mecanicamente, e um compilador LLM ligando cada fronteira, usável ponta a ponta por quem não é engenheiro. Um conjunto de artefatos estruturados, versionados em git, que capture — de forma encadeada — o que o storyboard, o blueprint, o EventStorming/Context Mapper e o XState/design system já capturavam separadamente, de forma que:

1. Um humano consiga ler, revisar e aprovar cada camada.
2. Um agente de IA consiga gerar o rascunho da camada N+1 a partir da camada N.
3. Uma mudança em qualquer camada propague de forma rastreável — e auditável — pelas camadas seguintes.
4. Lints entre camadas detectem incoerências mecanicamente (um edge case declarado no blueprint que nenhum fluxo trata; um evento de domínio que nenhuma tela dispara).

O LLM, nesse arranjo, não é o autor do produto. É o **compilador entre camadas** — e o humano é o gate de decisão em cada fronteira.

---

## 2. Princípios

**P1 — Toda camada é um artefato, todo artefato é um contrato.** Nada de decisão implícita. Se uma regra de negócio existe, ela está escrita em uma camada, com um ID. Se não está escrita, não existe — e o lint acusa o buraco.

**P2 — Rastreabilidade ponta a ponta.** Cada elemento carrega um ID estável e referencia os elementos das camadas anteriores que o justificam. Deve ser possível responder mecanicamente: "por que esta tela existe?" (→ fluxo → momento da jornada → FAQ do PRFAQ) e "o que quebra se eu remover esta regra?" (→ todas as telas, specs e testes que a referenciam).

**P3 — LLM como compilador, humano como gate.** A geração entre camadas é trabalho do agente; a aprovação é trabalho do humano. Nenhuma camada é considerada válida sem revisão explícita. Isso espelha o que as revisões de 6-pager faziam na Amazon — mas com o rascunho custando minutos, não semanas.

**P4 — Regeneração com diff, nunca reescrita.** Quando a camada N muda, as camadas N+1..k são *recompiladas* e o resultado é apresentado como diff sobre o que existia — preservando as decisões humanas já tomadas nas camadas posteriores que não conflitam com a mudança. Esse é o mesmo princípio do SDD maduro ("spec-anchored"), estendido para todo o pipeline.

**P5 — Fidelidade progressiva, formalidade constante.** As camadas iniciais são vagas em detalhes e precisas em intenção; as finais, o inverso. Mas todas são igualmente formais: um storyboard no Working Forward é vago sobre *telas* e exato sobre *momentos, atores e emoções*.

**P6 — O pipeline é bidirecional.** O caminho canônico é forward (visão → código), mas o framework prevê o caminho reverso: extrair a IR de um produto existente (código → fluxos → domínio → jornada) para trazê-lo para o regime. Produtos reais nascem dos dois lados.

**P7 — Handoff nativo para o ecossistema SDD.** Working Forward não compete com Spec Kit, Kiro ou BMAD — ele os alimenta. A última camada do framework *é* a entrada dos frameworks SDD. O que eles tratavam como ponto de partida (a spec escrita por alguém, de algum jeito), o Working Forward trata como saída compilada e rastreável.

---

## 3. As camadas

O Working Forward organiza o pipeline em sete camadas, L0 a L6. Cada uma tem: um propósito, uma linhagem (o artefato clássico que formaliza), um artefato canônico, um dono humano típico, e um contrato de entrada/saída com as vizinhas.

```
L0  VISÃO         prfaq.md + vision.yaml        (Amazon — Working Backwards)
L1  JORNADA       journey.yaml                  (Airbnb — storyboarding)
L2  SERVIÇO       blueprint.yaml                (service blueprint — Shostack, 1984)
L3  DOMÍNIO       domain.yaml                   (DDD — EventStorming)
L4  EXPERIÊNCIA   experience.yaml + tokens      (design systems)
L5  ESPECIFICAÇÃO specs/*.md                    (PRD, EARS, Gherkin)
L6  ARQUITETURA   → handoff SDD                 (Spec Kit, Kiro, BMAD, fde-kernel)
```

### L0 — Visão (linhagem: Amazon Working Backwards)

**Propósito.** Fixar o cliente, o problema, a solução em uma frase, e as perguntas difíceis — antes de qualquer decisão de produto.

**Artefatos.** O `prfaq.md` permanece narrativo, como a Amazon sempre defendeu: press release de uma página mais FAQ interna e externa. A narrativa é insubstituível — é onde o pensamento acontece. Mas o Working Forward acrescenta o `vision.yaml`: a extração estruturada do que o PRFAQ *afirma*, para que as camadas seguintes possam referenciá-lo.

```yaml
# vision.yaml (extraído do prfaq.md, revisado por humano)
product: aurora-tax
customer:
  primary: { id: CUST-01, who: "advogado tributarista sênior", context: "..." }
problem:
  - { id: PROB-01, statement: "monitorar 40+ normas/semana manualmente", severity: alta }
solution_one_liner: "..."
tenets:
  - { id: TEN-01, rule: "na dúvida, citar a fonte normativa — nunca parafrasear sem link" }
north_star: { metric: "consultas resolvidas sem escalação", target: "70% em 12m" }
hard_questions:          # as FAQs que definem escopo
  - { id: FAQ-07, q: "o que acontece quando duas normas conflitam?", owner_layer: L2 }
non_goals:
  - { id: NG-01, statement: "não é ferramenta de peticionamento" }
```

Repare no campo `owner_layer` das hard questions: cada pergunta difícil do PRFAQ é *endereçada* a uma camada. "O que acontece quando duas normas conflitam?" não se responde na visão — se responde no blueprint (L2), como regra de negócio. O lint do framework verifica que toda hard question foi consumida por sua camada dona. É a mecanização do que o bar raiser fazia na revisão do 6-pager: garantir que as perguntas difíceis não evaporem.

**Gate humano.** Founder / sponsor / PM. Nada avança sem PRFAQ aprovado — nisso, o Working Forward é ortodoxamente amazônico.

### L1 — Jornada (linhagem: Airbnb storyboarding)

**Propósito.** Transformar a promessa da visão em uma sequência de momentos vividos por atores reais — o que o projeto Snow White do Airbnb fez ao mapear a jornada de hóspedes e anfitriões em quadros, e descobrir que cada quadro era um domínio de investimento do produto.

**Artefato.** `journey.yaml` — atores, momentos, e para cada momento: intenção, emoção-alvo, canal, e o que o Airbnb chamava de "momento de verdade" (onde a experiência ganha ou perde o usuário).

```yaml
# journey.yaml
actors:
  - { id: ACT-ADV, name: "Advogado", persona_ref: CUST-01 }
  - { id: ACT-EST, name: "Estagiário", persona_ref: CUST-02 }
journeys:
  - id: JRN-CONSULTA
    actor: ACT-ADV
    trigger: "cliente pergunta sobre incidência de IBS em operação X"
    moments:
      - id: MOM-01
        name: "Formular a dúvida"
        intent: "traduzir a pergunta do cliente em consulta técnica"
        emotion_target: confiança
        channel: [web]
        truth_moment: false
      - id: MOM-03
        name: "Receber resposta fundamentada"
        intent: "obter resposta com base normativa citada"
        emotion_target: alívio
        truth_moment: true          # aqui o produto ganha ou perde
        vision_refs: [PROB-01, TEN-01]
```

**O que a camada NÃO decide:** telas, botões, endpoints. Um momento não é uma tela — frequentemente um momento vira três telas, ou meia. Essa disciplina (P5) é o que mantém a jornada estável enquanto a experiência itera.

**Gate humano.** Product design + PM. A pergunta da revisão: "essa é a história que queremos que o cliente conte?"

### L2 — Serviço (linhagem: service blueprinting — Shostack, 1984)

**Propósito.** Para cada momento da jornada, expor o iceberg: o que o usuário vê (frontstage), o que o sistema e a operação fazem (backstage), quais **regras de negócio** governam o passo, e — crucialmente — os **edge cases** e caminhos de falha. A técnica é de Lynn Shostack (*Harvard Business Review*, 1984) — a notação original que separa frontstage de backstage para desenhar serviços, quase 25 anos antes de existir um app de transporte para ilustrá-la. O Uber é citado aqui como exemplo didático, não como origem: um produto físico-digital onde motorista cancela, GPS falha e pricing muda em tempo real deixa a separação frontstage/backstage e o mapeamento de exceções como cidadãs de primeira classe particularmente fáceis de visualizar — mas a disciplina em si é do blueprint de Shostack.

**Artefato.** `blueprint.yaml` — por momento: frontstage, backstage, políticas, e edge cases com resolução declarada.

```yaml
# blueprint.yaml
blueprints:
  - moment_ref: MOM-03
    frontstage:
      - "resposta exibida com citações clicáveis por dispositivo normativo"
    backstage:
      - { id: BCK-11, action: "RAG sobre base LC 214/2025 + atos infralegais", sla_ms: 8000 }
      - { id: BCK-12, action: "validação de citação contra fonte primária" }
    policies:                        # regras de negócio COM identidade
      - id: POL-CIT-01
        rule: "toda afirmação normativa DEVE citar dispositivo verificado"
        source: TEN-01               # rastreia até o tenet da visão
        on_violation: "resposta é bloqueada e reformulada"
      - id: POL-CONF-01
        rule: "conflito entre normas exibe ambas + critério de resolução (hierarquia/cronologia/especialidade)"
        source: FAQ-07               # a hard question do PRFAQ, respondida aqui
    edge_cases:
      - id: EDG-05
        case: "base normativa desatualizada (norma publicada há <24h)"
        resolution: "responder com ressalva de vigência + agendar reindexação"
        severity: alta
      - id: EDG-06
        case: "pergunta fora do escopo tributário"
        resolution: "recusar com redirecionamento, citando NG-01"
```

**Por que esta camada é o coração do framework.** É aqui que mora quase tudo que as specs funcionais perdem: validações, políticas, exceções, SLAs, dependências operacionais. E é a camada com maior alavancagem de LLM: dado o `journey.yaml`, um agente é excelente em *propor* edge cases exaustivamente (é um gerador de casos adversariais por natureza) — e péssimo em decidir as resoluções, que são decisões de negócio. A divisão P3 é nítida: agente enumera, humano decide.

**Gate humano.** PM + ops + engenharia sênior, juntos. É a revisão mais cara do pipeline — e a mais barata comparada a descobrir os edge cases em produção.

### L3 — Domínio (linhagem: DDD / EventStorming)

**Propósito.** Extrair do blueprint a estrutura conceitual do sistema: eventos de negócio, comandos, agregados, políticas de reação, e as fronteiras — bounded contexts — que se tornarão fronteiras de arquitetura. O EventStorming de Brandolini sempre foi o artefato pré-IA mais próximo de uma IR de produto; o Working Forward o tira do post-it e o coloca no git.

**Artefato.** `domain.yaml`.

```yaml
# domain.yaml
events:
  - { id: EVT-ConsultaRespondida, aggregate: Consulta, emitted_by: BCK-11 }
  - { id: EVT-CitacaoInvalidada, aggregate: Consulta, emitted_by: BCK-12 }
commands:
  - { id: CMD-SubmeterConsulta, actor: ACT-ADV, produces: [EVT-ConsultaSubmetida] }
reactions:                # "policies" no vocabulário EventStorming
  - id: RCT-01
    when: EVT-CitacaoInvalidada
    then: CMD-ReformularResposta
    implements: POL-CIT-01           # rastreia até a regra do blueprint
aggregates:
  - { id: AGG-Consulta, invariants: [POL-CIT-01, POL-CONF-01] }
contexts:
  - id: CTX-Consultoria
    aggregates: [AGG-Consulta]
    moments_served: [MOM-01, MOM-03]
  - id: CTX-Monitoramento
    aggregates: [AGG-Norma]
    relationship: { with: CTX-Consultoria, type: upstream-published-language }
```

**O insight de rastreabilidade:** cada `reaction` implementa uma `policy` do L2; cada `invariant` de agregado referencia regras nomeadas. Quando a engenharia perguntar "por que o agregado Consulta bloqueia resposta sem citação?", a resposta é mecânica: `POL-CIT-01 ← TEN-01 ← prfaq.md`. A arquitetura herda a intenção com pedigree.

**Gate humano.** Engenharia sênior / arquitetura. Os bounded contexts decididos aqui viram serviços, módulos e times — é a decisão de maior custo de reversão do pipeline.

### L4 — Experiência (linhagem: design systems + máquinas de estado de UI)

**Propósito.** Materializar momentos em fluxos, fluxos em telas, telas em estados — com validações de interface derivadas das políticas de negócio, e vocabulário visual ancorado em tokens.

**Artefato.** `experience.yaml` (+ `tokens.json` no padrão W3C Design Tokens). A escolha estrutural decisiva: **fluxos são máquinas de estado**, não sequências de imagens. Estados, transições, guardas e efeitos — o mesmo formalismo de statecharts que a engenharia usa, aplicado à experiência.

```yaml
# experience.yaml
flows:
  - id: FLW-CONSULTA
    serves: [MOM-01, MOM-03]
    initial: compondo
    states:
      compondo:
        screen: SCR-EDITOR
        on:
          SUBMETER: { target: processando, guard: VAL-INPUT-01 }
      processando:
        screen: SCR-AGUARDE
        invoke: CMD-SubmeterConsulta       # amarra ao domínio (L3)
        on:
          EVT-ConsultaRespondida: { target: respondida }
          EVT-CitacaoInvalidada:  { target: reformulando }   # EDG visível na UI
          TIMEOUT_8S: { target: degradada } # honra o SLA de BCK-11
      respondida:
        screen: SCR-RESPOSTA
        must_render: [citacoes_clicaveis]  # frontstage de MOM-03
validations:
  - id: VAL-INPUT-01
    field: consulta.texto
    rule: "não-vazio, ≤ 4000 chars, idioma pt-BR detectado"
    derived_from: EDG-06               # fora de escopo → validação preventiva
screens:
  - id: SCR-RESPOSTA
    components: [resposta-card, citacao-chip, feedback-bar]
    tokens_scope: "consulta.*"
```

**O que este formalismo compra:** cada edge case do L2 precisa aparecer como estado ou transição em algum fluxo — e isso é lintável. O caminho triste deixa de ser o slide 47 que ninguém desenhou; ele é um estado nomeado com tela associada. E o par `experience.yaml` + `tokens.json` é exatamente o contrato que ferramentas design-to-code conseguem consumir para gerar UI real — ou, no sentido reverso (P6), o alvo que um extrator code-to-design produz a partir de um front-end existente.

**Gate humano.** Product design + front-end. A revisão pergunta duas coisas: "cada momento de verdade da jornada tem o cuidado que merece?" e "cada estado triste tem uma tela digna?"

### L5 — Especificação (linhagem: PRD, EARS, Gherkin)

**Propósito.** Compilar as camadas anteriores em specs funcionais por feature — o artefato que o ecossistema SDD espera receber.

**Artefato.** `specs/*.md`, com critérios de aceite em EARS, gerados majoritariamente por compilação. Uma spec do Working Forward é pouco escrita e muito *derivada*: o contexto vem da jornada, as regras vêm do blueprint, os eventos vêm do domínio, os fluxos vêm da experiência — a spec junta, com referências.

```markdown
# specs/consulta-fundamentada.md
Feature: Resposta fundamentada à consulta   [MOM-03, FLW-CONSULTA]

WHEN o sistema emite EVT-ConsultaRespondida
THE SYSTEM SHALL exibir cada afirmação normativa com citação clicável
  verificada contra fonte primária.                       [POL-CIT-01]

WHEN a validação de citação falha (EVT-CitacaoInvalidada)
THE SYSTEM SHALL transicionar FLW-CONSULTA para 'reformulando'
  sem exibir a resposta não verificada.                   [RCT-01, EDG-05]

IF a consulta estiver fora do escopo tributário
THEN THE SYSTEM SHALL recusar com redirecionamento.       [EDG-06, NG-01]
```

**Gate humano.** PM + tech lead. Como quase tudo é derivado, a revisão é leve — o trabalho pesado já foi aprovado camada a camada. Este é o dividendo do framework: a spec deixa de ser o lugar onde tudo se decide às pressas e vira o lugar onde tudo se *confirma*.

### L6 — Arquitetura e implementação (handoff)

O Working Forward termina onde o SDD começa, entregando três coisas aos frameworks da camada de implementação: as specs (L5) como entrada direta de Spec Kit/Kiro/BMAD; os bounded contexts (L3) como proposta de arquitetura; e as políticas e invariantes nomeadas como **suíte de enforcement** — no vocabulário do fde-kernel, os `invariants.toml` do produto, verificáveis em loop, commit e advisory. A eval suite de aceitação nasce das políticas do L2 e dos estados do L4, não de testes escritos depois do fato.

---

## 4. O compilador: LLMs entre camadas

### 4.1 As seis compilações

Cada fronteira entre camadas é uma operação de compilação com natureza própria — e com uma divisão de trabalho específica entre agente e humano:

| Fronteira | Operação | O agente é bom em | O humano decide |
|---|---|---|---|
| L0→L1 | narrativa → momentos | decompor a promessa em cenas, propor atores | quais momentos são de verdade |
| L1→L2 | momentos → iceberg | **enumerar edge cases exaustivamente**, propor backstage | resoluções, SLAs, trade-offs de negócio |
| L2→L3 | regras → modelo | extrair eventos/comandos do blueprint, propor agregados | fronteiras de contexto (custo de reversão!) |
| L3+L2→L4 | modelo → statecharts | gerar fluxos que cobrem todos os edge cases, mapear telas | hierarquia visual, momentos de cuidado, tom |
| L4+…→L5 | tudo → specs | compilação quase total (EARS derivado) | confirmação e priorização |
| L5→L6 | specs → código | o que o SDD já resolveu | revisão de código, promoção |

Duas fronteiras merecem destaque. **L1→L2 é onde o LLM tem alavancagem máxima**: enumerar modos de falha é geração adversarial, tarefa em que modelos são sistematicamente melhores que humanos sob pressão de prazo — enquanto decidir o que fazer em cada falha é julgamento de negócio puro. E **L2→L3 é onde o gate humano tem valor máximo**: bounded contexts errados custam re-arquitetura; nenhuma fluência de agente compensa aprovar essa camada no piloto automático.

### 4.2 Regeneração e diff (o protocolo de mudança)

Mudanças reais não começam no L0 — começam no meio ("jurídico decidiu que a resolução do EDG-05 muda"). O protocolo:

1. **Editar a camada dona.** A mudança é feita onde o elemento vive (EDG-05 está no L2).
2. **Marcar o cone de impacto.** O grafo de referências identifica tudo que aponta para EDG-05 nas camadas seguintes (estados do L4, cláusulas do L5, testes do L6).
3. **Recompilar só o cone.** O agente regenera os elementos impactados, propondo diffs — nunca reescrevendo camadas inteiras.
4. **Gates em cascata.** Cada diff passa pelo gate humano da camada correspondente. Um diff pequeno em L2 pode gerar diffs triviais em L4/L5 — a revisão é proporcional ao impacto real, não ao tamanho do pipeline.
5. **Commit atômico.** A mudança inteira — todas as camadas — entra num único commit/PR. O histórico do git conta a história do produto por decisões, não por arquivos.

### 4.3 Lints entre camadas (o sistema imunológico)

A rastreabilidade por IDs permite verificação mecânica de coerência. Lints mínimos do framework:

- **Cobertura de hard questions:** toda `hard_question` do L0 foi consumida pela sua `owner_layer`.
- **Cobertura de edge cases:** todo `EDG-*` do L2 aparece em ≥1 estado/transição do L4 ou é explicitamente marcado `accepted_risk` (com dono e data).
- **Fechamento de eventos:** todo evento do L3 é emitido por algum backstage e consumido por alguma reaction ou fluxo — eventos órfãos acusam modelagem morta.
- **Ancoragem de validações:** toda `validation` do L4 deriva de uma `policy` ou `edge_case` — validações sem pedigree são decisões clandestinas.
- **Specs completas:** toda cláusula EARS do L5 referencia ≥1 ID de camada anterior — cláusula sem referência é escopo inventado na compilação.
- **Não-objetivos respeitados:** nenhum fluxo/tela serve um `non_goal` do L0.

Esses lints rodam em CI como qualquer outro check. No vocabulário de enforcement em três níveis (loop / commit / advisory): cobertura de edge cases e ancoragem de validações são nível commit; o resto pode começar advisory e endurecer com a maturidade do time.

---

## 5. Níveis de maturidade

Espelhando a escada do SDD (spec-first / spec-anchored / spec-as-source), o Working Forward define três regimes de adoção:

**WF-1 · Vision-First.** As camadas são usadas uma vez, no zero-to-one, para chegar a specs de qualidade — e depois o código anda sozinho. Sem regeneração, sem lints em CI. Custo mínimo, valor real: mesmo descartável, o pipeline força as decisões a existirem. Adequado a protótipos e validações de mercado.

**WF-2 · Layer-Anchored (o sweet spot).** As camadas vivem no repositório junto do código, mudanças seguem o protocolo de regeneração, lints rodam em CI. O produto e sua IR evoluem juntos, com drift detectado mecanicamente. É o regime recomendado para produtos em produção com time dedicado.

**WF-3 · IR-as-Source.** As camadas são a única fonte da verdade; specs, testes de aceitação e porções crescentes do código e da UI são artefatos gerados. Hoje é fronteira — depende de design-to-code confiável (L4→UI) e de SDD maduro (L5→código) operando em cadeia. É a aposta de longo prazo do framework.

---

## 6. Papéis e cerimônias

O framework redefine menos os papéis do que os **pontos de encontro**:

- **Sponsor/Founder** — dono do L0. Cerimônia: revisão de PRFAQ (herdada da Amazon, intacta).
- **Product Manager** — fio condutor de L0–L2 e L5. Deixa de escrever PRDs do zero e passa a curar compilações.
- **Product Designer** — dono de L1 e L4. O storyboard volta a ser artefato central (não deck de kickoff que morre), e o Figma vira *renderização* do `experience.yaml`, não a fonte da verdade.
- **Engenharia sênior** — dona do L3 e do gate L2→L3. O EventStorming vira sessão de revisão do `domain.yaml` proposto pelo agente, não workshop de post-its de dois dias.
- **Agentes** — um por fronteira de compilação, com prompts e contratos próprios (análogo à separação de papéis do BMAD, mas organizados por *camada*, não por persona profissional).

A cerimônia central é o **Layer Review**: análoga ao code review, mas por camada, com o checklist do gate correspondente. A regra cultural: *não se discute tela em revisão de jornada, não se discute negócio em revisão de fluxo* — cada decisão tem sua camada, e discussões fora de camada são registradas como issues na camada certa.

---

## 7. Working Forward × o ecossistema

| | Escopo | O que formaliza | Relação com WF |
|---|---|---|---|
| **Working Backwards/PRFAQ** | visão | narrativa | absorvido como L0 |
| **Storyboarding (Airbnb)** | jornada | nada (visual) | formalizado como L1 |
| **Service Blueprint (Shostack, 1984)** | operação | nada (diagrama) | formalizado como L2 |
| **EventStorming/DDD** | domínio | semi (workshop) | formalizado como L3 |
| **Context Mapper/CML** | domínio | sim — DSL textual para bounded contexts e relações upstream/downstream, desde ~2018 | absorvido em L3: o `domain.yaml` usa o mesmo vocabulário de relação (`upstream-published-language`) que o CML já formalizava, só que confinado a times de arquitetura |
| **BPMN** | processo | sim — padrão OMG, notação textual/XML para fluxos de processo, desde 2011 | complementar, não absorvido: BPMN modela o fluxograma do processo de negócio; L2/L3 modelam momento + regra + evento, um recorte diferente do mesmo território |
| **Gherkin/Cucumber** | critério de aceite | sim — texto estruturado (Given/When/Then), machine-readable desde ~2007 | absorvido em L5: EARS é o dialeto do WF, mas o par pergunta/resposta é o mesmo que Gherkin já resolvia |
| **Example Mapping (Matt Wynne)** | descoberta de regras e exemplos | não — técnica de workshop colaborativo, sem artefato persistente por padrão | próximo em espírito de L2: descobre regras e edge cases antes de escrever critério de aceite, exatamente o que o blueprint faz — mas o blueprint persiste o resultado como YAML versionado e referenciável, não como cartões de sessão |
| **Design systems/tokens** | UI | tokens (visual) apenas; statecharts (Harel 1987) e XState/SCXML já formalizavam estados/transições/guardas de interface, só que como ferramenta de engenharia de front-end | tokens estendidos em L4; o formalismo de statecharts é adotado diretamente, não inventado |
| **Spec Kit / Kiro / BMAD** | spec→código | specs e tasks | jusante — consomem L5 |
| **fde-kernel e afins** | enforcement | invariantes | recebem as políticas como invariantes |
| **Figma Make / UX Pilot** | protótipo | nada (output visual) | renderizadores possíveis de L4 |

A leitura da tabela não é que a formalização nunca existiu — para domínio, processo, experiência e critério de aceite, ela existe há anos, em DSLs e notações de engenharia (Context Mapper, BPMN, XState, Gherkin) que nunca saíram do mundo de quem programa. O que faltava não era notação; era **encadeamento**: cada técnica resolve uma camada isolada, com seu próprio formato, sua própria ferramenta, seu próprio público — sem IDs que atravessem camadas, sem lint que verifique coerência entre elas, sem um caminho que uma pessoa de produto ou design consiga percorrer sem aprender a sintaxe de um compilador de estados. O Working Forward não inventa as ideias de baixo — o quadro acima deixa isso claro — inventa a **coluna que faltava**: uma cadeia única, referenciada por ID, lintada mecanicamente entre camadas, compilada por LLM, e utilizável ponta a ponta por quem não é engenheiro.

---

## 8. Limitações e questões abertas

Um reference guide honesto declara o que não sabe:

**Custo de cerimônia.** Sete camadas com gates humanos é peso real. O framework aposta que a compilação por LLM reduz o custo de *produção* de cada camada a ponto de o custo de *revisão* dominar — e revisão é exatamente onde humanos sêniores rendem mais. Mas essa aposta precisa de validação empírica; para times de 2–3 pessoas, WF-1 é o teto razoável.

**Expressividade do YAML.** Schemas estruturados capturam decisões, não sensibilidade estética. O L4 formaliza estados e validações; não formaliza *por que essa tela emociona*. O framework mitiga mantendo artefatos narrativos e visuais como anexos referenciados — mas a tensão entre formalidade e expressividade é permanente.

**Fidelidade da compilação.** A qualidade do rascunho L(N+1) depende do modelo, do prompt do agente da fronteira e da riqueza da camada N. O framework precisa de um benchmark próprio: dado um `journey.yaml` de referência, quão completo é o blueprint gerado? (Análogo direto aos evals de SDD.)

**Produtos não-transacionais.** As camadas L1–L2 assumem jornadas com começo, meio e fim. Produtos de engajamento contínuo (feeds, jogos, ferramentas criativas) mapeiam pior — a jornada vira loops, e a semântica de `truth_moment` precisa de extensão.

**Versionamento de schema.** Os schemas deste guide são v0. A evolução deles (campos novos, semânticas novas) precisa da mesma disciplina de compatibilidade de qualquer IR — o que sugere que o framework precisa, ele próprio, de uma spec formal e de uma suíte de conformidade.

---

## 9. Conclusão

Durante vinte anos, as melhores empresas de produto do mundo resolveram o caminho da visão ao código com artefatos brilhantes e desconexos, costurados pelo julgamento de gente sênior. A IA generativa tornou esse arranjo simultaneamente obsoleto e, pela primeira vez, formalizável: obsoleto porque as pontas automatizadas expõem o meio artesanal como gargalo; formalizável porque o custo de produzir e regenerar artefatos estruturados colapsou.

O Working Forward propõe que o design de produto ganhe o que o código sempre teve — representação formal, versionamento, diffs, lints, rastreabilidade — sem perder o que o tornou humano: a narrativa do PRFAQ, o cuidado do storyboard, o realismo do blueprint, o rigor do domínio. O LLM compila; o humano decide; o git lembra.

A Amazon ensinou o mundo a trabalhar de trás pra frente até a clareza. Está na hora de aprender a trabalhar pra frente a partir dela.

---

## Apêndice A — Estrutura de repositório de referência

```
product/
├── L0-vision/
│   ├── prfaq.md
│   └── vision.yaml
├── L1-journey/journey.yaml
├── L2-service/blueprint.yaml
├── L3-domain/domain.yaml
├── L4-experience/
│   ├── experience.yaml
│   ├── tokens.json
│   └── refs/                  # anexos visuais (Figma exports, moodboards)
├── L5-specs/*.md
├── lints/wf-lints.yaml        # configuração dos checks de coerência
└── agents/                    # prompts dos compiladores por fronteira
    ├── l0-to-l1.md
    ├── l1-to-l2.md
    └── ...
```

## Apêndice B — Checklist de gates (resumo)

- **G0 (visão):** cliente nomeado? problema com severidade? hard questions endereçadas a camadas? non-goals explícitos?
- **G1 (jornada):** todo momento tem intenção e emoção? momentos de verdade marcados? nenhum momento é uma tela disfarçada?
- **G2 (serviço):** toda hard question de L2 respondida como policy? todo edge case tem resolução ou accepted_risk? SLAs onde importa?
- **G3 (domínio):** todo evento tem emissor e consumidor? invariantes referenciam policies? fronteiras de contexto justificadas por acoplamento real?
- **G4 (experiência):** todo edge case coberto por estado/transição? toda validação com pedigree? estados tristes com telas dignas?
- **G5 (specs):** toda cláusula com referência? nada de escopo novo? priorização feita?

---

*Working Forward v0.1 — documento vivo. Feedback, forks e adversarial reviews são o método, não a exceção.*
