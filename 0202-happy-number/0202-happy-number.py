class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        new = 0
        while True: 
            while n > 0:
                new += (n % 10) ** 2
                n = n // 10
            if new == 1:
                return True
            if new in seen: 
                return False
            n = new
            seen.add(n)
            new = 0
            
            