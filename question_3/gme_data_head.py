import yfinance as yf

# Download GameStop stock data
gme_data = yf.download('GME')

# Reset the index
gme_data_reset = gme_data.reset_index()

# Display the first five rows
print(gme_data_reset.head())

# Save the screenshot
import matplotlib.pyplot as plt

# Create a simple plot to save as an image
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
tbl = ax.table(cellText=gme_data_reset.head().values, colLabels=gme_data_reset.columns, cellLoc='center', loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# Save the table as an image
plt.savefig('gme_data_head.png')
