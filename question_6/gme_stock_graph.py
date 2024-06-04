import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Download GameStop stock data
try:
    gme_data = yf.download('GME')
except Exception as e:
    print("Error:", e)

# Check if the DataFrame is not empty and the 'Close' column is present
if not gme_data.empty and 'Close' in gme_data.columns:
    # Plot GameStop stock graph with title
    make_graph(gme_data, 'GameStop Stock Price')
else:
    print("Unable to plot the graph due to missing data.")
