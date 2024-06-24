import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Read CSV file and sort data alphabetically by "name-id" column
csv_path = 'Dados Trilha + Familias\Abund Trilha.csv'
data = pd.read_csv(csv_path, encoding='ISO-8859-1')

df = pd.DataFrame(data)
df.sort_values(by='name-id', inplace=True)

# Set index to "name-id" column
df.set_index('name-id', inplace=True)

# Transpose DataFrame
df_transposed = df.transpose()

# Custom colors for bars
cores_barras = ['#235475', '#874001', '#228022', '#871b1c', '#60427a', '#8c564b']

# Create bar chart with custom colors
ax = df_transposed.plot(kind='bar', figsize=(10, 6), width=0.5, rot=0, color=cores_barras)

# Set log scale for y-axis and display real values
ax.set_yscale('log')
ax.yaxis.set_major_formatter(ScalarFormatter())

plt.title('Abundância por Trilha').set_fontsize(13)
plt.ylabel('Abundância (Log)').set_fontsize(12)
plt.legend(title='Família', bbox_to_anchor=(1, 1), loc='upper left')

# Set the order of the x-axis based on the sorted index
ax.set_xticks(range(len(df_transposed.index)))
ax.set_xticklabels(df_transposed.index.tolist(), rotation=0)

# Add values above each bar, including 0 values
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.annotate(str(int(height)), (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

# Save plot to file
plt.savefig('TCC - Fig 4 (Abund - Trilha).png', bbox_inches='tight', dpi=256)

# Show plot
plt.show()