class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        dic = defaultdict(int) # {num: frequency}
        for n in nums:
            dic[n] += 1
        freq = sorted(dic.values(), reverse=True)
        ans = []
        for i in range(0, k):
            x = list(dic.keys())[list(dic.values()).index(freq[i])]
            ans.append(x)
            del dic[x]
        return ans