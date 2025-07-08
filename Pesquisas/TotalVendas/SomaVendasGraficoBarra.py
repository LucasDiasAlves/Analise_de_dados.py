import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

# --- Para tirar o faturamento total de cada loja 

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

faturamento_numerico = dados.groupby('loja_id')['Preço'].sum()

plt.figure(figsize=(12, 8))

barras = plt.bar(faturamento_numerico.index, faturamento_numerico.values, color=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728'])

plt.title('Faturamento Total por Loja', fontsize=16)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=0) 

# Formata o eixo Y para exibir como moeda
formatter = mtick.StrMethodFormatter('R$ {x:,.2f}') # Formata com 2 casas decimais
plt.gca().yaxis.set_major_formatter(formatter)

# --- Adicionar Rótulos no Topo das Barras Verticais 
for barra in barras:
    altura = barra.get_height()
    plt.text(
        x=barra.get_x() + barra.get_width() / 2, 
        y=altura + 0.05, 
        s=f'R$ {altura:,.2f}', 
        ha='center', 
        va='bottom'  
    )

plt.tight_layout()
plt.show()