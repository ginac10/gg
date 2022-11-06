anagrams = {} # {"abc": ["bac", "bca"]}
if len(strs) == 0:
return [[""]]
elif len(strs) == 1:
return [strs]
else:
for word in strs:
if "".join(sorted(word)) in anagrams.keys():
anagrams[''.join(sorted(word))].append(word)
else:
anagrams[''.join(sorted(word))] = [word]
return anagrams.values()