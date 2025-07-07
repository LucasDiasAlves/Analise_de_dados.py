import matplotlib.pyplot as plt
import pandas as pd

# --- PASSO 1: Carregar e preparar os dados (exatamente como no primeiro código) ---
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

# Agrupar os dados por loja para obter o faturamento total de cada uma
faturamento_por_loja = dados.groupby('loja_id')['Preço'].sum()


# --- PASSO 2: Criar o Gráfico de Pizza ---

# Define o tamanho da figura
plt.figure(figsize=(10, 8))

# Define as cores (opcional, para manter consistência com o gráfico de barras)
cores = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']

# Lógica para "explodir" (destacar) a maior fatia
explode = [0] * len(faturamento_por_loja)  # Cria uma lista de zeros
indice_maior_fatia = faturamento_por_loja.idxmax() # Encontra o nome da loja com maior faturamento
posicao_maior_fatia = faturamento_por_loja.index.get_loc(indice_maior_fatia) # Encontra a posição numérica
explode[posicao_maior_fatia] = 0.1  # Define o destaque para a maior fatia

# Cria o gráfico de pizza
plt.pie(
    faturamento_por_loja,
    labels=faturamento_por_loja.index,
    autopct='%1.1f%%',  # Formato para exibir a porcentagem com uma casa decimal
    startangle=140,     # Ângulo inicial para melhor visualização
    colors=cores,
    explode=explode,    # Aplica o destaque na maior fatia
    shadow=True         # Adiciona uma sombra para um efeito 3D sutil
)

# Adiciona um título ao gráfico
plt.title('Distribuição Percentual do Faturamento por Loja', fontsize=16)

# Garante que o gráfico seja um círculo perfeito
plt.axis('equal')

# Exibe o gráfico
plt.show()