"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.
"""

prices = [2, 1, 2, 1, 0, 1, 2]

maxP = 0
l, r = 0, 1

while r < len(prices):
    profit = prices[r] - prices[l]
    if profit < 0:
        l = r
    maxP = max(profit, maxP)
    r += 1

print(maxP)
