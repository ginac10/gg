**Initial Solution**
problem: time
```
ans = []
rest = 1
before = 1
for i in range(len(nums)):
for j in range(i+1, len(nums)):
rest *= nums[j]
ans.append(before * rest)
before *= nums[i]
rest = 1
return ans
```
**Better Approach**:
arr -> and arr <-
See the space complexity hint -- should use the output arr.