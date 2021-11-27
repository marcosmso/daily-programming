"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple
transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2: return 0
        
        left = n * [0]
        buy, sell = 0, 1
        while sell < n:
            left[sell] = left[sell-1]
            if prices[sell] > prices[buy]:
                left[sell] = max(left[sell], prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
                sell = sell + 1
        
        right = n * [0]
        buy, sell = n-2, n-1 
        while buy >= 0:
            right[buy] = right[buy+1]
            if prices[buy] < prices[sell]:
                right[buy] = max(right[buy], prices[sell] - prices[buy])
                buy -= 1
            else:
                sell = buy
                buy = buy - 1
        
        max_profit = 0
        for i in range(n-1):
            max_profit = max(max_profit, left[i] + right[i+1])
        
        return max([max_profit, left[-1], right[0]])
