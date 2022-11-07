**Initial Solution**
```
dic = defaultdict(int) # {num: frequency}
for n in nums:
dic[n] += 1
freq = sorted(dic.values(), reverse=True)
ans = []
for i in range(0, k):
x = list(dic.keys())[list(dic.values()).index(freq[i])]
ans.append(x)
del dic[x]
return ans
```
**Bucketsort**
https://www.youtube.com/watch?v=YPTqKIgVk-k&t=2s