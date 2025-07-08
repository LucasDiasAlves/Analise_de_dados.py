import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

# --- verificando os produtos mais e menos vendidos

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

# --- conectando cada base url com sua respctiva loja
loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja['loja_id'] = 'loja_1'
loja2['loja_id'] = 'loja_2'
loja3['loja_id'] = 'loja_3'
loja4['loja_id'] = 'loja_4'

# --- concatenado os dados das lojas
dados = pd.concat([loja, loja2, loja3, loja4])

MaiseMenosVendidos = dados['Produto'].value_counts()

plt.figure(figsize=(15, 8)) # --- (plt.barh) organiza o grafico na horizontal, foi escolhido assim pelo numero de produtos
barras = plt.barh(MaiseMenosVendidos.index, MaiseMenosVendidos.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', "#2E5A14", "#1DBDE6", "#FF9595", "#000000"])

# --- títulos 
plt.title('Produtos mais e menos vendidos', fontsize=16)
plt.ylabel('Produto', fontsize=12)
plt.xlabel('Numero de vendas ', fontsize=12)
plt.xticks(rotation=0) # Mantém os nomes das lojas na horizontal

for barra in barras:
    # Pega a largura da barra (que é o número de vendas)
    largura = barra.get_width()

    # Adiciona o texto 
    plt.text(
        x=largura + 0.3,  # Posição X: um pouco à direita do final da barra
        y=barra.get_y() + barra.get_height() / 2,  # Posição Y: no centro vertical da barra
        s=f'{int(largura)}',  # O texto a ser exibido (o número de vendas como inteiro)
        va='center',  # Alinhamento vertical
        ha='left'     # Alinhamento horizontal
    )

plt.tight_layout()
plt.show()