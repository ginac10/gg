**Initial Approach** ig what I was tryint to do was use sets bc no dupes & unordered, and then "retrieve" the removed dupes for the triples, but i think no bueno
```
# nums.sort() # [-4, -1, -1, 0, 1, 2] # actually, I don't see how two-pointer would work here.
ans = set({}) # set, unique
for i in range(len(nums)):
for j in range(i+1, len(nums)):
for k in range(j+1, len(nums)):
if nums[i] + nums[j] + nums[k] == 0:
ans.add(set({nums[i], nums[j], nums[k]})) # need to deal w dupes
sol = []
for a in ans: # a = {-1, 2}
if len(a) == 1:
sol.append([a[0], a[0], a[0]])
elif len(a) == 2:
b = - (a[0] + a[1])
sol.append([a[0], a[1], b])
else:
sol.append([a[0], a[1], a[2]])
return sol
```