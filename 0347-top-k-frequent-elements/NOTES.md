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
​
```
class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
if k == len(nums): # Speeds up; 0(1) time
return nums
count = {} # {num : frequency}
dic =  [[] for i in range(len(nums) + 1)] # [[][][]...]
for n in nums:
count[n] = 1 + count.get(n, 0)
for n, c in count.items():
dic[c].append(n)
# freq = sorted(dic.values(), reverse=True)
ans = []
for i in range(len(dic) - 1, 0, -1):
for n in dic[i]:
ans.append(n)
if len(ans) == k:
return ans
```