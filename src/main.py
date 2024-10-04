import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtém o diretório de trabalho atual
diretorio_atual = os.getcwd()

# Constrói os caminhos dos arquivos
caminho_faixa = os.path.join(diretorio_atual, './data/dados_na_faixa.csv')
caminho_fora_faixa = os.path.join(diretorio_atual, './data/dados_fora_faixa.csv')

# Verifica se os arquivos existem
if not os.path.exists(caminho_faixa):
    print(f"Arquivo não encontrado: {caminho_faixa}")
    exit()

if not os.path.exists(caminho_fora_faixa):
    print(f"Arquivo não encontrado: {caminho_fora_faixa}")
    exit()

# Carregar os dados
dados_faixa = pd.read_csv(caminho_faixa)
dados_fora_faixa = pd.read_csv(caminho_fora_faixa)

# Remover espaços em branco dos nomes das colunas
dados_faixa.columns = dados_faixa.columns.str.strip()
dados_fora_faixa.columns = dados_fora_faixa.columns.str.strip()

# Calcular a média de desempenho entre Português e Matemática
dados_faixa['media_desempenho'] = (dados_faixa['desempenho_portugues'] + dados_faixa['desempenho_matematica']) / 2
dados_fora_faixa['media_desempenho'] = (dados_fora_faixa['desempenho_portugues'] + dados_fora_faixa['desempenho_matematica']) / 2

# Obter etapas
etapas = dados_faixa['etapa'].unique()

# Definir largura das barras
largura_barra = 0.35
indice = range(len(etapas))  # Posições das barras no eixo X

# Criar gráfico de barras
plt.figure(figsize=(10, 6))

# Barras para alunos na faixa etária
plt.bar(indice, dados_faixa.groupby('etapa')['media_desempenho'].mean(), 
        width=largura_barra, label='Na faixa etária', color='blue')

# Barras para alunos fora da faixa etária
plt.bar([i + largura_barra for i in indice], 
        dados_fora_faixa.groupby('etapa')['media_desempenho'].mean(), 
        width=largura_barra, label='Fora da faixa etária', color='red')

# Adicionar rótulos e título
plt.xlabel('Etapa')
plt.ylabel('Desempenho Médio')
plt.title('Comparação de Desempenho: Alunos Na Faixa Etária vs Fora da Faixa Etária')

# Adicionar ticks com os nomes das etapas
plt.xticks([i + largura_barra / 2 for i in indice], etapas)

# Adicionar legenda
plt.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

# Salvar o gráfico
caminho_grafico = os.path.join(diretorio_atual, './reports/comparacao_desempenho.png')
plt.savefig(caminho_grafico)

print(f"Gráfico salvo em: {caminho_grafico}")
