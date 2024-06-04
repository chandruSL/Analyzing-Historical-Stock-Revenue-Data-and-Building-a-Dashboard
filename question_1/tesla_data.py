import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download Tesla stock data
tesla_data = yf.download('TSLA')

# Reset the index
tesla_data_reset = tesla_data.reset_index()

# Display the first five rows
print(tesla_data_reset.head())

# Create a simple plot to save as an image
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
tbl = ax.table(cellText=tesla_data_reset.head().values, colLabels=tesla_data_reset.columns, cellLoc='center', loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# Save the table as an image to the current directory
plt.savefig('tesla_data_head.png')
