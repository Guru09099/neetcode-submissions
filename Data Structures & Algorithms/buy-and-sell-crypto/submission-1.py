class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_day = 999
        profit = 0
        for i in prices:
            min_day = min(min_day, i)
            diff = i - min_day
            profit = max(profit, diff)
        return profit 
        