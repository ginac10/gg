class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        i = 0
        while i + 1 < len(prices):
            total += max(0, prices[i+1]-prices[i])
            i += 1
        
        return total