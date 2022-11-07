class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): # Speeds up; 0(1) time
            return nums
        
        count = {} # {num : frequency}
        dic =  [[] for i in range(len(nums) + 1)] # [[][][]...]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            dic[c].append(n)
        # freq = sorted(dic.values(), reverse=True)
        
        ans = []
        for i in range(len(dic) - 1, 0, -1):
            for n in dic[i]:
                ans.append(n)
            if len(ans) == k:
                return ans