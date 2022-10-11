class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):#you want to do the index, not the number
            want = target - nums[i]
            if want in seen:#.items:
                return [i, seen[want]]#.index(want)]
            seen[nums[i]] = i
            ##^ THIS IS BC it's easier to see KEYS in dictionary!