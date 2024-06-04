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

# Download Tesla stock data
try:
    tesla_data = yf.download('TSLA')
except Exception as e:
    print("Error:", e)

# Check if the DataFrame is not empty and the 'Date' column is present
if not tesla_data.empty and 'Close' in tesla_data.columns:
    # Plot Tesla stock graph with title
    make_graph(tesla_data, 'Tesla Stock Price')
else:
    print("Unable to plot the graph due to missing data.")

