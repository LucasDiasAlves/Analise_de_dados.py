import matplotlib.pyplot as plt
import pandas as pd

# --- Gera grafico de extremos, os produtos mais e menos vendidos

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

MaiseMenosVendidos = dados['Produto'].value_counts()
N = 10 # Número de produtos a serem mostrados em cada extremo

# --- Ordena os dados
MaiseMenosVendidos = MaiseMenosVendidos.sort_values(ascending=False)

# --- Seleciona o top N e o Botton N
top_N = MaiseMenosVendidos.head(N)
bottom_N = MaiseMenosVendidos.tail(N)

# --- Concatena os dois para plotar no mesmo gráfico
dados_extremos = pd.concat([top_N, bottom_N])
dados_extremos = dados_extremos.sort_values(ascending=True)

# --- Criação do Gráfico ---
plt.figure(figsize=(12, 12))
cores = ['lightcoral'] * N + ['mediumseagreen'] * N
barras = plt.barh(dados_extremos.index, dados_extremos.values, color=cores)

# Títulos e rótulos
plt.title(f'Top {N} e Bottom {N} Produtos Mais Vendidos', fontsize=18)
plt.xlabel('Número de Vendas', fontsize=12)
plt.ylabel('Produto', fontsize=12)

# Adicionar o número de vendas no final de cada barra
for barra in barras:
    largura = barra.get_width()
    plt.text(largura + 2,
             barra.get_y() + barra.get_height() / 2,
             f'{int(largura)}',
             ha='left',
             va='center')

# Ajusta a margem esquerda para garantir que os nomes dos produtos não sejam cortados
plt.subplots_adjust(left=0.1)

# O tight_layout ainda é útil para ajustar o resto
plt.tight_layout(rect=[0, 0, 1, 1]) # O rect ajuda a tight_layout a respeitar o subplots_adjust

plt.show()