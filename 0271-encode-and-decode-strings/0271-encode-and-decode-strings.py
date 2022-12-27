class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        
        # Edge case: if # is > 1 digit...
        while s:
            upTo = s.index("#")
            if upTo == -1:
                return result
            
            take = int(s[0:upTo])
            s = s[upTo+1:]
            result.append(s[0:take])
            s = s[take:]
            
        
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))