class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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