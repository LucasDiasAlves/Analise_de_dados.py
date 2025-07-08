import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter   # Personalizar números dos eixos com segurança
import pandas as pd

# --- Soma de total de vendas das 4 lojas em barra empilhada

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

faturamento_pivot = dados.pivot_table(
    index='Categoria do Produto',
    columns='loja_id',
    values='Preço',
    aggfunc='sum'
).fillna(0)


# --- Função que formata os números como moeda
def currency_formatter(x, pos):
    return f'R$ {x:,.0f}'

# Usar a função de plotagem do Pandas com stacked=True
ax = faturamento_pivot.plot(
    kind='bar',
    stacked=True,
    figsize=(14, 8),
    colormap='viridis'
)

# Adicionar títulos e rótulos
ax.set_title('Faturamento por Categoria de Produto (Empilhado por Loja)', fontsize=16)
ax.set_xlabel('Categoria do Produto', fontsize=12)
ax.set_ylabel('Faturamento (R$)', fontsize=12)

formatter = FuncFormatter(currency_formatter)
ax.yaxis.set_major_formatter(formatter)

ax.legend(title='Lojas')

# Rotacionar os rótulos do eixo X para melhor leitura
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()