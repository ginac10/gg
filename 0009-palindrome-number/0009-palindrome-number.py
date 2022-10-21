class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        half = len(strX)//2
        front = strX[0:half]
        back = strX[::-1][0:half]
        return front == back

        