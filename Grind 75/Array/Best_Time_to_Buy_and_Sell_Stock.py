# Brute force solution
def findStock(prices):
  max_profit = 0
  n = len(prices)
  for i in range(n-1):
    for j in range(i+1, n):
      if prices[j] < prices[i]:
        continue
      current_profit = prices[j] - prices[i]
      if current_profit > max_profit:
        max_profit = current_profit

  return max_profit

# Optimize solution
def maxProfit(prices):
  max_profit = 0
  buy = prices[0]
  for sell in prices[1:]:
    if sell > buy:
      max_profit = max(max_profit, sell - buy)
    else:
      buy = sell
  
  return max_profit

prices = [7,6,4,3,1]
res = findStock(prices)
print(res)
res2 = maxProfit(prices)
print(res2)

