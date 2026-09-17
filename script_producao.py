import pandas as pd
import numpy as np
import sqlite3

# 1. GERANDO A BASE DE DADOS DE SCOUTING ATUALIZADA
np.random.seed(42)
n_jogadores = 250

nacionalidades = ['Brasileiro', 'Argentino', 'Uruguaio', 'Colombiano', 'Uruguaio']

dados_scouting_atualizado = {
    'jogador_id': range(1001, 1001 + n_jogadores),
    'nome': [f'Jovem Talento {i}' for i in range(n_jogadores)],
    'nacionalidade': np.random.choice(nacionalidades, n_jogadores, p=[0.4, 0.2, 0.15, 0.15, 0.1]),
    'idade': np.random.randint(17, 24, n_jogadores),
    'clube_atual': np.random.choice(['Base Palmeiras', 'Envigado FC', 'Base Flamengo', 'Nordsjælland', 'Jong Ajax', 'Base Santos'], n_jogadores),
    'posicao': np.random.choice(['Meio-Campista', 'Ponta Direita', 'Zagueiro', 'Volante'], n_jogadores),
    'minutos_jogados': np.random.randint(900, 2800, n_jogadores),
    'passes_progressivos_por_90': np.random.uniform(2.1, 8.5, n_jogadores).round(2),
    'acoes_criacao_chute_por_90': np.random.uniform(1.5, 5.2, n_jogadores).round(2),
    'desarmes_ganhos_por_90': np.random.uniform(0.8, 4.1, n_jogadores).round(2)
}

df_novo = pd.DataFrame(dados_scouting_atualizado)

# 2. SALVANDO NO BANCO DE DADOS SQL
conexao = sqlite3.connect('scouting_futebol.db')
df_novo.to_sql('promessas', conexao, if_exists='replace', index=False)
print("💾 Banco de dados SQL 'scouting_futebol.db' criado com sucesso!")

# 3. EXECUTANDO A QUERY SQL PARA MAPEAMENTO DE BRASILEIROS
query_brasileiros = """
SELECT nome, nacionalidade, idade, clube_atual, passes_progressivos_por_90, acoes_criacao_chute_por_90
FROM promessas
WHERE posicao = 'Meio-Campista' 
  AND nacionalidade = 'Brasileiro'
  AND idade <= 21 
  AND minutos_jogados >= 1000
  AND passes_progressivos_por_90 > 4.5
ORDER BY acoes_criacao_chute_por_90 DESC;
"""

shortlist_brasileiros = pd.read_sql_query(query_brasileiros, conexao)
conexao.close()

print("\n🇧🇷 PROSPECÇÃO: MEIO-CAMPISTAS BRASILEIROS SUB-21 ENCONTRADOS:")
print(shortlist_brasileiros)

# 4. EXPORTANDO O RELATÓRIO PARA EXCEL
shortlist_brasileiros.to_excel('relatorio_scouting_brasileiros.xlsx', index=False)
print("\n📊 Relatório 'relatorio_scouting_brasileiros.xlsx' exportado para a pasta!")
