class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nset = set(nums)
        maxx = 0
        # curr = 1
        
        for x in nset:
            if x-1 not in nset: #this means it's the start of a streak
                curr = 1
                while x + curr in nset:
                    curr += 1
                maxx = max(curr, maxx)
        return maxx
                