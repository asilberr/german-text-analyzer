import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Path to CSV file
## TODO: Change the file path to the location of the CSV file generated in the previous step
input_file_path = '/'

# Read the CSV file
word_freq_df = pd.read_csv(input_file_path)

# Create a Wordcloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(zip(word_freq_df['Wort'], word_freq_df['Anzahl'])))

# Plot the Wordcloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Wordcloud der Worthäufigkeiten')
plt.show()

# Save the Wordcloud as an image
## TODO: Change the output path to the desired location
output_wordcloud_path = '/'
plt.savefig(output_wordcloud_path, dpi=300, bbox_inches='tight')
plt.show()

# Create a Bubble Chart
# Filter the DataFrame to only include words with a frequency of 4 or more
filtered_df = word_freq_df[word_freq_df['Anzahl'] >= 4]

# Plot the Bubble Chart
fig, ax = plt.subplots(figsize=(10, 6))

# Create a color mapping for the bubble colors
norm = Normalize(vmin=filtered_df['Anzahl'].min(), vmax=filtered_df['Anzahl'].max())
sm = ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])

# Plot the bubbles
scatter = ax.scatter(filtered_df['Wort'], filtered_df['Anzahl'], s=filtered_df['Anzahl']*100, c=filtered_df['Anzahl'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)

# Add annotations to the bubbles
for i, word in enumerate(filtered_df['Wort']):
    ax.text(filtered_df['Wort'].iloc[i], filtered_df['Anzahl'].iloc[i], word, ha='center', va='center', fontsize=9)

# Add colorbar
cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.02, pad=0.04)
cbar.ax.yaxis.set_label_position('right')
cbar.ax.yaxis.tick_right()

# Title and labels
ax.set_title('Gefiltertes Bubble Chart der Worthäufigkeiten', fontsize=14, fontweight='bold')
ax.set_xlabel('Wort')
ax.set_ylabel('Anzahl')
plt.xticks(rotation=45, ha='right')

# Save the Bubble Chart as an image
## TODO: Change the output path to the desired location
output_bubble_chart_path = '/'
plt.savefig(output_bubble_chart_path, dpi=300, bbox_inches='tight')
plt.show()

print(f"Bubble Chart wurde als Bild in {output_bubble_chart_path} gespeichert.")