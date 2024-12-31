import yfinance as yf
from colorama import Fore
import time

stock = yf.Ticker(input("Enter a Ticker: "))
data = stock.history(period="ytd")  # Last month of data

data['Percent Change'] = data['Close'].pct_change() * 100

open = False
datePrice = 0
funds = 10_000
startFunds = funds

buyLimit = float(input("What should be the buy barrier: "))
sellLimit = float(input("What should be the sell barrier: "))


print("Days when we bought:")
for i in range(1, len(data)):
    if not open:
        if data['Percent Change'].iloc[i] <= -buyLimit:
            print("-------------")
            print(Fore.RED)
            print(data.index[i].date(), f"{data['Percent Change'].iloc[i]:.2f}%")
            open = True
            datePrice = data["Close"].iloc[i]
    else:
        funds += funds * (data["Percent Change"].iloc[i] / 100)
        # print((data["Close"].iloc[i] - data["Close"].iloc[i-1]) / data["Close"].iloc[i-1] )
        # print(data["Percent Change"].iloc[i])
        if ((data["Close"].iloc[i] - datePrice) / datePrice) * 100 > sellLimit:
            open = False
            print(Fore.GREEN)
            print(f"Sold on: {data.index[i].date()}") 

            print(f"percent earned: {((data["Close"].iloc[i] - datePrice) / datePrice) *100:.1f}")

            print(f"Funds available: {funds:.2f}")
            print(Fore.RESET)
            print("-------------")
            # time.sleep(1)

print(Fore.MAGENTA)
print("End of data\n\n")
print(Fore.YELLOW)
print("Money made with strategy: ")
print(f"{funds - startFunds:.2f}")
print(f"Total funds: {funds:.2f}")
print(Fore.RESET)
