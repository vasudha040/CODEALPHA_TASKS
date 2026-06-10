# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

num_stocks = int(input("How many stocks do you want to enter? "))

for i in range(num_stocks):
    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio.txt")