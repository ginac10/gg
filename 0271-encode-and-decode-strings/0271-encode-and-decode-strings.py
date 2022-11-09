class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        sol = ""
        for s in strs:
            sol += str(len(s)) + "#" + s # You have to have "#" in case of ##s
        return sol

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            ans.append(s[j+1:j+1+num])
            i = j + num + 1
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))