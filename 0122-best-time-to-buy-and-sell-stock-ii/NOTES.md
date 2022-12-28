Previous.... this problem was too easy.
​
#i = 0
#curr = prices[i]
#while i+1 > len(prices):
#    curr = prices[i]
#    if curr < prices[i+1]:
#        total+=prices[i+1]-curr
#        i+=1
#    else:
#        total += max(0, prices[i+1]-curr)
#        i+=1