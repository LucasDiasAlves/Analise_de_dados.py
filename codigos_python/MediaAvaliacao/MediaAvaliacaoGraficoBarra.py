import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter  # Importação recomendada
import pandas as pd

# --- Tirando a media de avaliação de cada loja

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

media_avaliacao = dados.groupby('loja_id')['Avaliação da compra'].mean()

plt.figure(figsize=(12, 8))
barras = plt.bar(media_avaliacao.index, media_avaliacao.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# --- Títulos
plt.title('Média de Avaliação de Cada Loja', fontsize=16)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Média da Avaliação', fontsize=12)
plt.xticks(rotation=0)

# --- Função para exibir no eixo y o valor com números decimais
def decimal_formatter(x, pos):
    return f'{x:.2f}'

formatter = FuncFormatter(decimal_formatter)
plt.gca().yaxis.set_major_formatter(formatter)

# --- Laço for para adicionar o valor com duas casas decimais em cima de cada barra, com sua respectiva loja
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval + 0.01, f'{yval:.2f}', va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()