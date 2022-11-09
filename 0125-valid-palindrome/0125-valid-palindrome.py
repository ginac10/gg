class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase, remove non alpha# (regex)
        s = s.lower()
        s = re.sub(r'[\W_]+', '', s)
        #print(s)
        #print(s[::-1])
        return s == s[::-1]
        