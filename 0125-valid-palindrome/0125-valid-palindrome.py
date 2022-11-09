class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase, remove non alpha# (regex)
        s = s.lower()
        s = re.sub(r'[\W_]+', '', s)
        return s == s[::-1]
        