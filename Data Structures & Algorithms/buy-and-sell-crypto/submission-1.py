class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            j = i+1
            while j < len(prices):
                profit = prices[j] - prices[i]
                if profit < 0:
                    i = j-1
                    break
                if max_profit < profit:
                    max_profit = profit
                j += 1
            i += 1
        return max_profit
            
                    
        