import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file and sort data alphabetically by "Famílias" column
csv_path = 'Dados Trilha + Familias\Abund T.csv'
family_data = pd.read_csv(csv_path, encoding='ISO-8859-1').sort_values(by='Famílias')

# Set index to "Famílias" column
family_data.set_index('Famílias', inplace=True)

# Custom colors
colors = ['#235475', '#874001', '#228022', '#871b1c', '#60427a', '#8c564b']

# Create subplot
fig, ax = plt.subplots(figsize=(10, len(family_data.index)))

# Create bar chart with custom colors
family_data['Total'].plot(kind='bar', ax=ax, color=colors)

# Set log scale for y-axis
ax.set_yscale('log')

plt.title('Abundância Total das Famílias')
plt.ylabel('Abundância Total (Log)')

# Add values above each bar
for p in ax.patches:
    height = p.get_height()
    ax.annotate(str(int(height)), (p.get_x() + p.get_width() / 2., height),
                 ha='center', va='center', xytext=(0, 4), textcoords='offset points', fontsize=10)

# Set y-axis tick labels to absolute values
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Rotate x-axis tick labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Save plot to file
plt.savefig('TCC - Fig 3 (Abund Total).png', bbox_inches='tight', dpi=256)

# Show plot
plt.show()