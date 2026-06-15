"""
Dune Retraction and Urban Expansion Correlation
Visualizes the relationship between coastal squeeze (urbanization) and dune area loss.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Dissertation Dataset (2004 - 2024)
data = {
    'Year': [2004, 2012, 2015, 2020, 2024],
    'Urban_Area_ha': [91.43, 96.41, 102.39, 103.39, 111.37],
    'Dune_Area_ha': [146.06, 128.02, 126.35, 136.52, 118.82]
}
df = pd.DataFrame(data)

# Plotting Configuration
fig, ax1 = plt.subplots(figsize=(10, 6))

# Axis 1: Dune Area
color1 = '#d7191c' # Red for retraction
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Dune Area (ha)', color=color1, fontsize=12, fontweight='bold')
line1, = ax1.plot(df['Year'], df['Dune_Area_ha'], color=color1, marker='o', linewidth=2.5, label='Dune Area')
ax1.tick_params(axis='y', labelcolor=color1)

# Axis 2: Urban Area (Twin X)
ax2 = ax1.twinx()
color2 = '#2c7bb6' # Blue for urban expansion
ax2.set_ylabel('Urban Area (ha)', color=color2, fontsize=12, fontweight='bold')
line2, = ax2.plot(df['Year'], df['Urban_Area_ha'], color=color2, marker='s', linewidth=2.5, linestyle='--', label='Urban Area')
ax2.tick_params(axis='y', labelcolor=color2)

# Title and Legend
plt.title('Correlation: Dune Retraction vs Urban Expansion (Coastal Squeeze)', fontsize=14, pad=15, fontweight='bold')
ax1.legend(handles=[line1, line2], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=True)

plt.tight_layout()

# Save the output
output_path = 'coastal_squeeze_correlation.png'
plt.savefig(output_path, dpi=300)
print(f"Chart successfully saved to {output_path}")

plt.show()
