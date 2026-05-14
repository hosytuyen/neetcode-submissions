class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_before_today = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - min_before_today
            if max_profit < profit:
                max_profit = profit
            min_before_today = min(prices[i], min_before_today)
        return max_profit
            
                    
        