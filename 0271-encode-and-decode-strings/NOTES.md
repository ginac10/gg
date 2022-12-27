**More clever approach** -- chunked transfer encoding, but not w bytes as leet sol.
Reminders:
- can't concatenate int to str
​
```
class Codec:
def encode(self, strs: List[str]) -> str:
"""Encodes a list of strings to a single string.
"""
sol = ""
for s in strs:
sol += str(len(s)) + "#" + s # You have to have "#" in case of ##s
return sol
​
def decode(self, s: str) -> List[str]:
"""Decodes a single string to a list of strings.
"""
ans, i = [], 0
while i < len(s):
j = i
while s[j] != "#":
j += 1
num = int(s[i:j])
ans.append(s[j+1:j+1+num])
i = j + num + 1
return ans
​
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```
​
**Naive Solution (Initial Attempt)**
```
def encode(self, strs: List[str]) -> str:
"""Encodes a list of strings to a single string.
"""
str = ""
for s in strs:
str += s + "라"
return str
​
def decode(self, s: str) -> List[str]:
"""Decodes a single string to a list of strings.
"""
strs = []
temp = ""
for c in s:
if c != '라':
temp += c
else:
strs.append(temp)
temp = ""