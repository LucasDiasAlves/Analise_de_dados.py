import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas
import geobr


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


#  --- Carregar o mapa-múndi a partir do arquivo local .shp
try:
    estados_br = geobr.read_state(year=2020)
    print("Malha de estados do Brasil carregada com sucesso via geobr!")
except Exception as e:
    print(f"Não foi possível baixar os dados dos estados: {e}")
    print("Verifique sua conexão com a internet.")
    exit()

# --- Criar a figura e os eixos do gráfico (nosso "quadro" em branco)
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# --- CAMADA 1: Desenhando o mapa dos estados no fundo ---
estados_br.plot(
    ax=ax,
    color='whitesmoke', # Cor de preenchimento dos estados
    edgecolor='gray',   # Cor das linhas das divisas
    linewidth=0.7       # Espessura das linhas das divisas
)

# --- CAMADA 2: Desenhando o mapa de densidade (calor) por cima ---
sns.kdeplot(
    data=dados,
    x='lon',
    y='lat',
    ax=ax,              # Garante que o calor seja desenhado no mesmo quadro do mapa
    fill=True,
    thresh=0.05,
    alpha=0.6,          # Usamos transparência para ver as divisas por baixo
    cmap="plasma"
)

# 3. Ajustar os limites do mapa para um bom enquadramento
#    (não é estritamente necessário, pois o plot dos estados já ajusta, mas é uma boa prática)
ax.set_xlim(-75, -34)
ax.set_ylim(-35, 6)

# 4. Títulos e rótulos
ax.set_title('Mapa de Densidade de Vendas por Estado', fontsize=18)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_aspect('equal') # Garante que a proporção do mapa não fique distorcida

plt.show()