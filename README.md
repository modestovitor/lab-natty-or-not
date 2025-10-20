# 🤖 Natty or Not: IA no Futuro dos Concursos Públicos 🇧🇷

> Projeto prático mostrando como **IA generativa** eleva a qualidade e a eficiência de uma **banca de concursos** — da **fábrica de questões** à **comunicação institucional** — com **curadoria humana** e trilhas auditáveis.

---

## 📜 Descrição

Este projeto demonstra, com base em experiências reais, como **modelos de linguagem (LLMs)** e ferramentas complementares transformam processos que vão da **elaboração de provas e questões** até a **comunicação com candidatos e órgãos públicos**.
Mais do que “apenas IA”, evidenciamos o papel **estratégico**: **reduzir custo e tempo**, **padronizar linguagem e documentos**, **aumentar transparência** e **melhorar a experiência** do candidato.
O resultado é um fluxo **prático, auditável e replicável**, sempre com **Human-in-the-Loop (HITL)**.

---

## 🤖 Tecnologias Utilizadas

* 🧬 **LLM (GPT)** — geração/apoio a textos técnicos (itens, pareceres, e-mails).
* 🛠️ **GitHub** — versionamento, colaboração e portfólio.
* ⚙️ **Python** — automação e geração de saídas em Markdown (script gerador).
* ☁️ **AWS PartyRock** *(sobre **Amazon Bedrock**)* — protótipo público para **gerar e auditar questões**.

> Observação: **Amazon Bedrock** é o serviço de modelos gerenciados da AWS; **PartyRock** é o playground que roda **sobre** o Bedrock.

---

## 🧩 Protótipo no AWS PartyRock

* **App:** *Questionário Pro*
* **Link público:** [https://partyrock.aws/u/ModestoVitor/5PZtj8gaj/Questionario-Pro](https://partyrock.aws/u/ModestoVitor/5PZtj8gaj/Questionario-Pro)
* **Captura (opcional):** `docs/partyrock/print-01.png`

**O que faz**

* Entrada: tipo de questão (objetiva A–E), área do conhecimento, tema e nível (B/I/A).
* Diretrizes: tom institucional, **distratores plausíveis** e **rationale obrigatório**.
* Saída: **enunciado + A–E (1 correta) + gabarito + rationale + análise dos distratores**.
* Refino: via chat (ajustar nível, remover pistas, citar norma, etc.).

> A saída do app pode ser colada em `exemplos/QUESTOES.md` ou salva como `exemplos/QUESTOES_GERADAS.md`.

---

## 🧪 Processo de Criação

1. **Mapeamento de dores reais**: elaboração de itens, padronização de linguagem, análise de recursos e comunicação institucional.
2. **Prompts estruturados por tarefa**: itens objetivos, comunicados, e-mails e pareceres.
3. **Diretrizes de qualidade**: dificuldade calibrada, **distratores verossímeis**, **rationale** e tom **institucional**.
4. **Curadoria Humana (HITL)**: revisão técnica/jurídica e linguística antes da publicação.
5. **Documentação**: exemplos em Markdown e script que gera saídas auditáveis.

---

## ▶️ Execução do Gerador (opcional)

O script `exemplos/src/generate_questions.py` produz questões **no padrão deste projeto**.
Funciona **sem IA** (modo demonstração) e **com IA** (se `OPENAI_API_KEY` estiver definida).

**Modo 1 — Sem IA (demonstração)**

```bash
python exemplos/src/generate_questions.py \
  --tema "Transparência e Comunicação" \
  --nivel Intermediário \
  --n 2 \
  --saida exemplos/QUESTOES_GERADAS.md
```

**Modo 2 — Com IA (quando houver chave)**

```bash
export OPENAI_API_KEY="sua_chave"
python exemplos/src/generate_questions.py \
  --tema "Transparência e Comunicação" \
  --nivel Intermediário \
  --n 5 \
  --saida exemplos/QUESTOES_GERADAS.md
```

> Boas práticas: **HITL sempre**; em RAG, manter **corpus controlado**, versionamento e **rastreabilidade de fontes**.

---

## 🧪 Exemplos de Aplicação

* `exemplos/QUESTOES.md` — itens gerados/curados com **gabarito**, **rationale** e **análise de distratores**.
* `exemplos/EMAIL.md` — **modelo de e-mail institucional** (tom formal).
* `exemplos/PARTYROCK.md` — documentação do **app PartyRock** (fluxo + exemplo de saída).

---

## 🗂️ Estrutura do Projeto

```bash
lab-natty-or-not/
├── README.md
├── docs/
│   └── partyrock/
│       └── print-01.png              # evidência visual do protótipo (opcional)
├── exemplos/
│   ├── QUESTOES.md                   # questões curadas (rationale + distratores)
│   ├── EMAIL.md                      # modelo de e-mail institucional
│   ├── RELATORIO.md                  # (opcional) roteiro de parecer/relatório
│   ├── QUESTOES_GERADAS.md           # (opcional) amostra de saída do gerador
│   ├── PARTYROCK.md                  # documentação do app PartyRock
│   └── src/
│       └── generate_questions.py     # gerador de itens (com/sem IA) → Markdown
└── .gitignore / LICENSE              # opcionais (higiene e licença)
```

---

## 📊 Resultados Alcançados

* 📈 **Itens auditáveis** com nível controlado e distratores verossímeis.
* 🧾 **Padronização documental** (e-mails, ofícios, minutas).
* ⏱️ **Redução de esforço** em tarefas repetitivas.
* 🏛️ **Transparência** e melhor experiência do candidato.

---

## 🔒 Qualidade & Governança

* **Rationale obrigatório** + **análise de distratores** em cada item.
* **Curadoria humana** antes da publicação.
* Linguagem **institucional**, sem vieses e sem pistas óbvias.
* Em RAG: **corpus controlado**, versionado e com **fontes rastreáveis**.

---

## 🚀 Próximos Passos

1. **PartyRock/Bedrock** — protótipo para **posts “Edital Disponível”** (arte + legenda + link oficial) com identidade visual da banca.
2. **Automação social** — agendas de **publicações periódicas** (arte + legenda), com trilha de aprovação.
3. **Provas completas** — geração assistida por **RAG**, revisão por pares e auditoria de fontes.
4. **Pipeline de IA** — do conteúdo à publicação e **análise de desempenho** (ciclo de feedback).

---

## 💭 Reflexão Final

O **“Natty ou Not”** aqui não é sobre “parecer IA”, mas sobre **resolver problemas reais** com qualidade acima do padrão, **ética**, **auditoria** e **curadoria**.
Com **AWS PartyRock/Bedrock** e o **gerador em Python**, abrimos espaço para protótipos que unem tecnologia, comunicação e eficiência, elevando o padrão dos processos seletivos no Brasil.

---

## 📄 Licença

Este repositório está licenciado sob a **MIT License**. Consulte o arquivo `LICENSE` para detalhes.
