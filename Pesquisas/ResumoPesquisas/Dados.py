import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# --- Base url dos dados das lojas em arquivos csv
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

# --- Conectando cada base url com sua respctiva loja
loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

# --- Colocando uma "etiqueta" de identificação em cada conjunto de dados antes de "misturalos" ou em outras palavras concatenar.
loja['loja_id'] = 'loja_1'
loja2['loja_id'] = 'loja_2'
loja3['loja_id'] = 'loja_3'
loja4['loja_id'] = 'loja_4'

# --- Concatenando os dados das lojas
dados = pd.concat([loja, loja2, loja3, loja4])

# Soma da coluna 'Preço' para obter o valor total de vendas.
# --- Utilizando a concatenação dados e groupby, torna possivel conseguir o valor total de vendas de todas as 4 lojas em uma unica pesquisa
valor_total_vendas = dados.groupby('loja_id')['Preço'].sum()

# Conta o número de linhas para obter a quantidade de produtos vendidos.
quantidade_vendas = dados.groupby('loja_id')['Produto'].count()

# --- Verificar qual o produto é mais vendido
cat = dados['Categoria do Produto'].value_counts()

# --- Calcular a media de avaliação dos clientes
media = dados.groupby('loja_id')['Avaliação da compra'].mean()

# --- Calcular produtos mais e menos vendidos
prod = dados['Produto'].value_counts()

# --- Calcular a media do frete
frete = dados.groupby('loja_id')['Frete'].mean()

# 3. Exibir os resultados no terminal
print("--- Análise das 4 lojas ---")
print("------------------------------")
print(f"Quantidade de produtos vendidos: {quantidade_vendas + 1}") # --- O mais um no print é para mostrar o numero real de vendas, pois toda lista começa o 0 consta como o numero inicial, ou seja sem o +1 seriam 2359 ao inves de 2360
print("------------------------------")
print(f"Valor total de vendas: R$ {valor_total_vendas}")
print("------------------------------")
print("\n--- Lista de Categorias ---")

print(cat) #lista de categoria de produto é mais vendido
print("\n--- media de avalização de compras ---")
print(media.round(2)) #media de avaliação de compra
print("\n--- Vendas de cada produto ---")
print(prod) #lista de numero de vendas de cada produto
print("\n--- media de fretes ---")
print(frete) #media do frete