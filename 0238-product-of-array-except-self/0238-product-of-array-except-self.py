class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        f = 1
        b = 1
        for i in range(len(nums)):
            ans[i] = f
            f *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= b
            b *= nums[j]
        return ans