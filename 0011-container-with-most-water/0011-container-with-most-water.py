class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxx = min(height[p1], height[p2]) * (p2-p1)
        a = 0
        
        while p1 < p2:
            a = min(height[p1], height[p2]) * (p2-p1)
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            if a > maxx:
                maxx = a
        return maxx
    