import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Leitura dos dados do primeiro CSV
df_clima = pd.read_csv('Dados Trilha + Familias\Dados.csv')

# Transposição do DataFrame para facilitar o plot
df_clima_t = df_clima.transpose()
df_clima_t.columns = df_clima_t.iloc[0]
df_clima_t = df_clima_t[1:]
df_clima_t = df_clima_t.astype(float)

# Leitura dos dados do segundo CSV
csv_path = 'Dados Trilha + Familias\Abund1.csv'
data_abundancia = pd.read_csv(csv_path, encoding='ISO-8859-1')
df_abundancia = pd.DataFrame(data_abundancia)
df_abundancia.set_index('name-id', inplace=True)
df_abundancia_transposed = df_abundancia.transpose()

# Cores desejadas para as barras
cores_barras = ['#235475', '#874001', '#228022']
cores_linhas = ['#ff6f00', '#2b00ff', '#0dff00']

# Criando subplots
fig, ax2 = plt.subplots(figsize=(10, 6))

# Plotando o gráfico de barras no segundo subplot com cores específicas
df_abundancia_transposed.plot(kind='bar', ax=ax2, width=0.4, position=0.5, color=cores_barras, legend=False)

# Adicionando título e rótulos aos eixos do segundo subplot
ax2.set_ylabel('Abundância')
ax2.set_xlabel('Família')

# Adicionando valores diretamente acima de cada barra no segundo subplot
for p in ax2.patches:
    height = p.get_height()
    ax2.annotate(str(int(height)), (p.get_x() + p.get_width() / 2., height),
                 ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# Rotacionar os rótulos das datas no eixo x para a horizontal
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)

# Criando o primeiro subplot
ax1 = ax2.twinx()

# Plotando o gráfico de linhas no primeiro subplot
for coluna, cor in zip(df_clima_t.columns, cores_linhas):
    if coluna == 'temp':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Temperatura (°C)', color=cor)
    elif coluna == 'precip':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Precipitação (mm)', color=cor)
    elif coluna == 'umidade':
        ax1.plot(df_clima_t.index, df_clima_t[coluna], label='Umidade (%)', color=cor)

ax1.set_yscale('log')  # Configurando a escala logarítmica no eixo y
# Formatando os rótulos do eixo y para exibir números absolutos
ax1.yaxis.set_major_formatter(ScalarFormatter())

# Adicionando título e rótulos aos eixos do primeiro subplot
ax1.set_ylabel('Valores Climáticos (Log)')
yticks = [20, 30, 100, 200, 300, 400]
plt.yticks(yticks)
#plt.ylim(15, 500)

# Adicionando a legenda manualmente para o subplot de Clima
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

# Adicionando a legenda manualmente para o subplot de Família
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines2, labels2, loc='upper left', bbox_to_anchor=(1.05, 0.85))

# Salvando o gráfico como um arquivo PNG
plt.savefig('TCC - Fig 5 (Clima + Abund1).png', bbox_inches='tight', dpi=256) 

# Exibindo o gráfico
plt.show()
