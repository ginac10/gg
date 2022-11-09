Original:
```
if len(nums) <= 1:
return len(nums)
nums.sort() # O(NlogN)
curr = 1 #0 # It should be one bc technically a # is a streak of 1
maxx = 1 #0
for i in range(len(nums)-1):
if nums[i] != nums[i+1]: # Can't forget abt this case -- should do nada
if nums[i] + 1 == nums[i+1]:
curr += 1
else:
if curr > maxx:
maxx = curr
curr = 1
return max(maxx, curr) # to account for last
```
​
Improvements:
* No need to increment i's to continuously check `nums[i] + 1 == nums[i+1]`. Instead, you can just check the next i, then increment ans and i.
​
More ingenious solution: https://www.youtube.com/embed/P6RZZMu_maU -- finding all the start values.