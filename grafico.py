import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd



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
# --- PASSO 1: Preparar os dados (garantir que são numéricos) ---
# Se você já executou este comando, pode pular. Estamos apenas garantindo
# que temos os dados brutos para o gráfico.
faturamento_numerico = dados.groupby('loja_id')['Preço'].sum()

# --- PASSO 2: Criar o Gráfico de Barras com Matplotlib ---

# Define o tamanho da figura (opcional, mas ajuda na visualização)
plt.figure(figsize=(10, 6))

# Cria o gráfico de barras
# .index pega os nomes das lojas (loja_1, loja_2, etc.)
# .values pega os valores de faturamento
barras = plt.bar(faturamento_numerico.index, faturamento_numerico.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Adiciona títulos e rótulos para clareza
plt.title('Faturamento Total por Loja', fontsize=16)
plt.xlabel('Lojas', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=0) # Mantém os nomes das lojas na horizontal

# Formata o eixo Y para exibir como moeda
formatter = mtick.FormatStrFormatter('R$ {:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

# Adiciona os rótulos de valor em cima de cada barra (opcional)
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval, f'R${yval:,.0f}', va='bottom', ha='center') # va='bottom' para o texto ficar acima da barra


# Otimiza o layout para que nada fique cortado
plt.tight_layout()

# Exibe o gráfico
plt.show()