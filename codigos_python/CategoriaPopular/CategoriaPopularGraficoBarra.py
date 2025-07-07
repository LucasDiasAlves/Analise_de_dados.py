import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

# --- verificando as categorias de produtos mais populares e seus numeros de vendas ---

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

# ---conectando cada base url com sua respctiva loja
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

mais_populares = dados['Categoria do Produto'].value_counts()


plt.figure(figsize=(12, 8))

barras = plt.bar(mais_populares.index, mais_populares.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', "#2E5A14", "#1DBDE6", "#FF9595", "#000000"])

# --- titulos para melhor vizualização 
plt.title('categorias de produtos mais populares', fontsize=16)
plt.xlabel('Categoria do Produto', fontsize=12)
plt.ylabel('Numero de vendas ', fontsize=12)
plt.xticks(rotation=0) # --- Mantém os nomes das lojas na horizontal


# --- Adiciona os rótulos de valor em cima de cada barra
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval, f'{yval:.0f}', va='bottom', ha='center') 


# Otimiza o layout para que nada fique cortado
plt.tight_layout()

# Exibe o gráfico
plt.show()