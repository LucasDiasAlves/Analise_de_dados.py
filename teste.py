import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter  # Importação recomendada
import pandas as pd

# --- URLs e Concatenação (sem alterações) ---
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja['loja_id'] = 'loja_1'
loja2['loja_id'] = 'loja_2'
loja3['loja_id'] = 'loja_3'
loja4['loja_id'] = 'loja_4'

dados = pd.concat([loja, loja2, loja3, loja4])

# --- PASSO 1: Preparar os dados (com correção no .mean()) ---
# CORREÇÃO 1: Removido o argumento inválido de .mean()
media_avaliacao = dados.groupby('loja_id')['Avaliação da compra'].mean()

# --- PASSO 2: Criar o Gráfico de Barras ---
plt.figure(figsize=(12, 8))
barras = plt.bar(media_avaliacao.index, media_avaliacao.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Títulos e rótulos
plt.title('Média de Avaliação de Cada Loja', fontsize=16)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Média da Avaliação', fontsize=12)
plt.xticks(rotation=0)

# CORREÇÃO 2: Formatando o eixo Y de forma segura com FuncFormatter
def decimal_formatter(x, pos):
    """Formata o número com 2 casas decimais."""
    return f'{x:.2f}'

formatter = FuncFormatter(decimal_formatter)
plt.gca().yaxis.set_major_formatter(formatter)

dados1 = pd.concat([loja, loja2, loja3, loja4])
# --- PASSO 1: Preparar os dados (garantir que são numéricos) ---
# Se você já executou este comando, pode pular. Estamos apenas garantindo
# que temos os dados brutos para o gráfico.
mais_populares = dados1['Categoria do Produto'].value_counts()

# --- PASSO 2: Criar o Gráfico de Barras com Matplotlib ---

# Define o tamanho da figura (opcional, mas ajuda na visualização)
plt.figure(figsize=(12, 8))

# Cria o gráfico de barras
# .index pega os nomes das lojas (loja_1, loja_2, etc.)
# .values pega os valores de faturamento
barras = plt.bar(mais_populares.index, mais_populares.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', "#2E5A14", "#1DBDE6", "#FF9595", "#000000"])

# Adiciona títulos e rótulos para clareza
plt.title('categorias de produtos mais populares', fontsize=16)
plt.xlabel('Categoria do Produto', fontsize=12)
plt.ylabel('Numero de vendas ', fontsize=12)
plt.xticks(rotation=0) # Mantém os nomes das lojas na horizontal

# Formata o eixo Y para exibir como moeda

# Adiciona os rótulos de valor em cima de cada barra (opcional)
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval, f'{yval:.0f}', va='bottom', ha='center') # va='bottom' para o texto ficar acima da barra


# CORREÇÃO 3: Adicionando os rótulos com 2 casas decimais em cima das barras
for barra in barras:
    yval = barra.get_height()
    # Alterado para ':.2f' para mostrar os decimais
    plt.text(barra.get_x() + barra.get_width()/2.0, yval + 0.01, f'{yval:.2f}', va='bottom', ha='center', fontsize=12)

# Otimiza o layout e exibe o gráfico
plt.tight_layout()
plt.show()