# ⚽ Mapeamento de Jovens Talentos Brasileiros (Sub-21) usando Python e SQL

## 🎯 Objetivo do Projeto
Este projeto simula o fluxo de trabalho real de um Analista de Mercado (Scouting) em um clube de futebol. O objetivo principal foi identificar meio-campistas brasileiros de até 21 anos com métricas de elite em progressão de jogo e criação de jogadas, otimizando o processo de captação de atletas sob a ótica da estratégia *Moneyball*.

## 🛠️ Tecnologias Utilizadas
* **Python**: Criação do ecossistema de dados, manipulação e limpeza com `Pandas` e `NumPy`.
* **SQL (SQLite)**: Armazenamento dos dados em banco relacional local e consultas estruturadas (Queries) para filtragem inteligente de mercado.
* **Matplotlib & Seaborn**: Criação de uma Matriz de Scouting (Scatter Plot) para análise visual de anomalias estatísticas.

## 🔍 Metodologia e Filtros Aplicados (SQL)
Para encontrar os atletas certos, foi executada uma query SQL simulando as regras de busca do repositório *FBref/StatsBomb*:
* **Posição:** Meio-Campista
* **Nacionalidade:** Brasileira
* **Idade:** ≤ 21 anos
* **Minutos Jogados:** ≥ 1000 min (garantindo amostragem confiável)
* **Passes Progressivos por 90 min:** > 4.5
* **Métrica de Decisão:** Ordenado por Ações de Criação de Chute por 90 min (Métrica de agressividade ofensiva).

## 📊 Principais Resultados (Shortlist de Negócios)
O projeto identificou com sucesso uma lista de 9 atletas com potencial de mercado, destacando:
1. **A Anomalia de Elite (ID 59 - Base Santos)**: Líder absoluto com 8.37 passes progressivos e 4.95 ações de criação de chute por 90 minutos aos 17 anos. Um perfil de elite raro de compra imediata.
2. **O Motor de Transição (ID 42 - Envigado FC)**: Atleta de 20 anos ideal para modelos de jogo verticais, com alta capacidade de fazer a bola chegar ao ataque (7.45 passes progressivos/90).

---
*Projeto desenvolvido como portfólio prático de transição de carreira após a conclusão do bootcamp da TripleTen.*
