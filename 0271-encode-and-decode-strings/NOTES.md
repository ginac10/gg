**More clever approach** -- chunked transfer encoding, but not w bytes as leet sol.
Reminders:
- can't concatenate int to str
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
return strs
```
Minor Improvement:
```
def encode(self, strs: List[str]) -> str:
... return str[:len(str) - 1]
​
def decode(self, s: str) -> List[str]:
... return s.split("라")
```