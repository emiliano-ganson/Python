import yfinance as yf
import matplotlib.pyplot as plt

# 1. Download S&P 500 data for 2025
print("Downloading data...")
data = yf.download("^GSPC", start="2025-01-01", end="2025-12-31")

# 2. Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], color='green', linewidth=2)

# Styling
plt.title('S&P-500 Performance - 2025', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True, linestyle='--', alpha=0.6)

# 3. Save the image
plt.savefig('sp500_2025.png')
print("Graph saved as sp500_2025.png")

# 4. SHOW the image on screen
print("Displaying graph...")

plt.show()
