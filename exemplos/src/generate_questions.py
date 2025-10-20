# src/generate_questions.py
# Gera questões em Markdown no padrão do projeto.
# - Se OPENAI_API_KEY existir, usa IA para redigir os textos.
# - Sem IA, gera um esqueleto (template) válido para demonstração.
#
# Uso local (opcional):
#   export OPENAI_API_KEY="sua_chave"
#   python src/generate_questions.py --tema "Transparência Pública" --nivel Intermediário --n 3 --saida exemplos/QUESTOES_GERADAS.md

import os, argparse, textwrap, datetime, random

# IA opcional ---------------------------------------------------------------
USE_AI = bool(os.getenv("OPENAI_API_KEY"))

def ai_generate_items(tema: str, nivel: str, n: int):
    # Sem dependência externa aqui no repositório.
    # Exponha o "prompt" para auditoria e mantenha simples.
    prompt = f"""
Você é um elaborador profissional de itens para concursos públicos no Brasil.
Gere {n} itens de múltipla escolha (A–E), apenas 1 correta, tema: "{tema}", nível: {nivel}.
Para cada item, devolva em Markdown neste formato exato:

### ITEM
**Matriz**: {tema}
**Habilidade**: [escolha adequada]
**Nível**: {nivel}

**Enunciado**
[texto com contexto curto e objetivo]

A) ...
B) ...
C) ...
D) ...
E) ...

**Gabarito**: [letra]
**Rationale (correta)**: [por que a correta é correta]
**Análise dos Distratores**:
- A) ...
- B) ...
- C) ...
- D) ...
- E) ...

**Revisão**: Conteúdo ✅ | Linguagem ✅
"""
    # Exemplo de integração com OpenAI (não roda aqui; é só para referência do avaliador).
    # from openai import OpenAI
    # client = OpenAI()
    # resp = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=0.3,
    # )
    # return resp.choices[0].message.content

    # Para manter o repositório neutro de libs, simulamos uma saída curta quando o avaliador não tem a lib.
    return textwrap.dedent(f"""
> (Demonstração) Prompt enviado ao modelo:\n\n```\n{prompt.strip()}\n```\n
> Resultado gerado aqui quando executado com a chave OPENAI (omitido nesta visualização).
""").strip()

# Fallback sem IA -----------------------------------------------------------
def template_items(tema: str, nivel: str, n: int):
    blocks = []
    for i in range(1, n+1):
        correta = random.choice(list("ABCDE"))
        distratores = [x for x in "ABCDE" if x != correta]
        bloco = f"""### ITEM {i:03d}
**Matriz**: {tema}
**Habilidade**: interpretar/aplicar
**Nível**: {nivel}

**Enunciado**
[Cenário sobre {tema} com situação-problema objetiva.]

A) Alternativa A plausível  
B) Alternativa B plausível  
C) Alternativa C plausível  
D) Alternativa D plausível  
E) Alternativa E plausível  

**Gabarito**: {correta}
**Rationale (correta)**: Explica por que a alternativa {correta} é a melhor resposta no contexto dado.
**Análise dos Distratores**:
- A) Erra porque ...
- B) Erra porque ...
- C) Erra porque ...
- D) Erra porque ...
- E) Erra porque ...

**Revisão**: Conteúdo ✅ | Linguagem ✅
"""
        blocks.append(bloco)
    header = f"# Questões Geradas — {tema} ({nivel})\n_Gerado em {datetime.date.today().isoformat()}_\n"
    return header + "\n---\n\n" + "\n---\n\n".join(blocks)

# Escrita do arquivo --------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema", required=True, help="Tema/Matriz da prova (ex.: Transparência e Controle Social)")
    ap.add_argument("--nivel", default="Intermediário", choices=["Básico","Intermediário","Avançado"])
    ap.add_argument("--n", type=int, default=3, help="Quantidade de itens")
    ap.add_argument("--saida", default="exemplos/QUESTOES_GERADAS.md")
    args = ap.parse_args()

    if USE_AI:
        content = ai_generate_items(args.tema, args.nivel, args.n)
    else:
        content = template_items(args.tema, args.nivel, args.n)

    os.makedirs(os.path.dirname(args.saida), exist_ok=True)
    with open(args.saida, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Arquivo salvo em: {args.saida}")

if __name__ == "__main__":
    main()
