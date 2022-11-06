class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = defaultdict(list) # defaultdict -- same as dict, no err
        for s in strs:
            count = [0] * 26 # a ... z
            for i in s:
                count[ord(i) - ord('a')] += 1 # ord -- char to int, unicode
            fin[tuple(count)].append(s) # convert to tuple bc list cannot be key in python
        return fin.values()