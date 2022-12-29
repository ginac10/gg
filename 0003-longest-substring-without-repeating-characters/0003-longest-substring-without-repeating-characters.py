class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window Problem 
        seen = set()
        longest = 0
        l = 0
        
        for r in range(len(s)):
            #if s[r] not in seen:
            #    seen.add(s[r])
            #else: # if in seen
            #    longest = max(longest, r - l)
            #    while s[l] != s[r]:
            #        l += 1
            #    l += 1
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r-l + 1)
                
        return longest