class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # windowLen - count[maxOccuringLetter]
            while (r-l+1) - max(count.values()) > k: # if invalid,
                count[s[l]] -= 1 # subtract
                l += 1 # typical when moving the window 
            
            ans = max(ans, r - l + 1)
        
        return ans
            