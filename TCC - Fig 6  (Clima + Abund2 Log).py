import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Leitura dos dados do primeiro CSV
df_clima = pd.read_csv('Dados.csv')

# Transposição do DataFrame para facilitar o plot
df_clima_t = df_clima.transpose()
df_clima_t.columns = df_clima_t.iloc[0]
df_clima_t = df_clima_t[1:]
df_clima_t = df_clima_t.astype(float)

# Leitura dos dados do segundo CSV
csv_path = 'Dados Glei\Abund2.csv'
data_abundancia = pd.read_csv(csv_path, encoding='ISO-8859-1')
df_abundancia = pd.DataFrame(data_abundancia)
df_abundancia.set_index('name-id', inplace=True)
df_abundancia_transposed = df_abundancia.transpose()

# Cores desejadas para as barras e linhas
cores_barras = ['#871b1c', '#60427a', '#8c564b']
cores_linhas = ['#ff6f00', '#2b00ff', '#0dff00']

# Criando subplots
fig, ax2 = plt.subplots(figsize=(10, 6))

# Plotando o gráfico de barras no segundo subplot em escala logarítmica com cores específicas
df_abundancia_transposed.plot(kind='bar', ax=ax2, width=0.4, position=0.5, color=cores_barras, legend=False)
ax2.set_yscale('log')  # Configurando a escala logarítmica no eixo y

# Adicionando título e rótulos aos eixos do segundo subplot
ax2.set_ylabel('Abundância (Log)')
ax2.set_xlabel('Família')

# Adicionando valores diretamente acima de cada barra no segundo subplot
for p in ax2.patches:
    height = p.get_height()
    if height > 0:
        ax2.annotate(f"{height:.0f}", (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# Formatando os rótulos do eixo y para exibir números absolutos
ax2.yaxis.set_major_formatter(ScalarFormatter())

# Rotacionar os rótulos das datas no eixo x para a horizontal
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)

# Criando o primeiro subplot
ax1 = ax2.twinx()

# Plotando o gráfico de linhas no primeiro subplot com cores específicas
for coluna, cor in zip(df_clima_t.columns, cores_linhas):
    if coluna == 'temp':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Temperatura (°C)', color=cor)
    elif coluna == 'precip':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Precipitação (mm)', color=cor)
    elif coluna == 'umidade':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Umidade (%)', color=cor)

# Adicionando título e rótulos aos eixos do primeiro subplot
ax1.set_ylabel('Valores Climáticos')

# Adicionando a legenda manualmente para o subplot de Clima
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

# Adicionando a legenda manualmente para o subplot de Família
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines2, labels2, loc='upper left', bbox_to_anchor=(1.05, 0.83))

# Salvando o gráfico como um arquivo PNG
plt.savefig('TCC - Fig 6  (Clima + Abund2 Log).png', bbox_inches='tight', dpi=2048) 

# Exibindo o gráfico
plt.show()
