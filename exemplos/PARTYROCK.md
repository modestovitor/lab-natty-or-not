# PartyRock — Questionário Pro (AWS Bedrock)

Protótipo público usado neste projeto para **gerar e auditar questões** com padrão institucional de banca.

- **Link do app:** https://partyrock.aws/u/ModestoVitor/5PZtj8gaj/Questionario-Pro  
- **Captura:** `../docs/partyrock/print-01.png` *(suba um print no repositório para este caminho, se desejar)*

## Fluxo do Protótipo
1. **Entrada**  
   - Tipo: objetiva (A–E)  
   - Área do conhecimento (ex.: Administração Pública, Direito Administrativo)  
   - Tema específico (ex.: “Transparência e Controle Social”)  
   - Parâmetros: nível (B/I/A), linguagem institucional e diretrizes de qualidade
2. **Saída**  
   - Enunciado + alternativas A–E (1 correta)  
   - **Gabarito**, **Rationale** (por que a correta é correta)  
   - **Análise dos Distratores** (por que cada incorreta erra)  
   - Observações de revisão (human-in-the-loop)
3. **Refino (chat)**  
   - Ajustar nível, plausibilidade dos distratores, remover pistas, adequar estilo/tom e citar norma quando aplicável.

## Exemplo resumido de saída
> **Tema:** Transparência e Controle Social (Intermediário)  
> **Enunciado:** Município adota painéis abertos e **auditoria contínua**. Assinale a correta:  
> A) Ativa substitui passiva.  
> B) Controle interno só a posteriori.  
> C) Auditoria contínua **fortalece** o controle social, mas **não substitui** transparência ativa e passiva.  
> D) Publicidade pode ser afastada por portaria.  
> E) Tempo real dispensa PPA/LDO/LOA.  
> **Gabarito:** C — **Rationale:** auditoria é complementar; deveres ativo/passivo permanecem.  
> **Distratores:** A/B/D/E incorretos por confundir deveres, suprimir prevenção, afastar princípio por ato infralegal e ignorar planejamento.

## Integração com o repositório
- Itens gerados são copiados para `exemplos/QUESTOES.md` (padrão do projeto)  
  ou salvos como `exemplos/QUESTOES_GERADAS.md`.  
- O script `exemplos/src/generate_questions.py` documenta o pipeline local (com/sem IA) e o **prompt** (auditável).

## Governança e Qualidade
- **Curadoria humana** obrigatória (human-in-the-loop).  
- Em cenários com RAG: **corpus controlado**, versionamento e **rastreabilidade de fontes**.  
- Padrões: validade de conteúdo, clareza, nível coerente, distratores plausíveis, rationale explícito.
