class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        
        for i, n in enumerate(nums):# enumerate is faster than range len!
            if i > 0 and n == nums[i-1]:
                continue            # cont to next iteration of the loop
            
            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                if n + nums[p1] + nums[p2] == 0:
                    sol.append([n, nums[p1], nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1 += 1
                if n + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                else: # <
                    p1 += 1
        return sol

    
    
#while initial <= len(nums) - 3:    
#while p1 < p2:
#    if initial + nums[p1] + nums[p2] == 0:
#        sol.append([initial, p1, p2])
#        if nums[p1] == nums[p1+1]:
#            p1 += 2
#        else:
#            p1 += 1
#        if nums[p2] == nums[p2-1]:
#            p2 -= 2
#        else: 
#            p2 -= 1
#    elif initial + nums[p1] + nums[p2] > 0:
#        if nums[p2] == nums[p2-1]:
#            p2 -= 2
#        else: 
#            p2 -= 1
#    else:
#        if nums[p1] == nums[p1+1]:
#            p1 += 2
#        else:
#            p1 += 1
#if nums[initial] == nums[initial + 1]:
#    initial += 2
#    p1 = initial + 1
#    p2 = len(nums) - 1    