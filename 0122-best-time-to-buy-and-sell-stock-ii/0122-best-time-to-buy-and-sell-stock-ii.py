class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        #i = 0
        #curr = prices[i] 
    
        #while i+1 > len(prices):
        #    curr = prices[i] 
        #    if curr < prices[i+1]:
        #        total+=prices[i+1]-curr
        #        i+=1
        #    else:
        #        total += max(0, prices[i+1]-curr)
        #        i+=1
        
        i = 0
        while i + 1 < len(prices):
            total += max(0, prices[i+1]-prices[i])
            i += 1
        
        return total