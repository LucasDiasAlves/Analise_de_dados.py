import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter  # --- Personalizar números dos eixos com segurança
import pandas as pd

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

media_avaliacao = dados.groupby('loja_id')['Frete'].mean()

plt.figure(figsize=(12, 8))
barras = plt.bar(media_avaliacao.index, media_avaliacao.values, color=['#d62728', '#ff7f0e', '#1f77b4', '#2ca02c' ])

# --- Títulos
plt.title('Média de frete de cada loja', fontsize=16)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Média do frete', fontsize=12)
plt.xticks(rotation=0)

def decimal_formatter(x, pos): # --- Função para organizar os textos do eixo y 
    return f'R$ {x:.2f}'
formatter = FuncFormatter(decimal_formatter)
plt.gca().yaxis.set_major_formatter(formatter)

# --- Para adicionar o respectivo valor de cada loja e adicionar 2 casas decimais
for barra in barras:
    yval = barra.get_height()

    plt.text(barra.get_x() + barra.get_width()/2.0, yval + 0.01, f'R$ {yval:.2f}', va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()