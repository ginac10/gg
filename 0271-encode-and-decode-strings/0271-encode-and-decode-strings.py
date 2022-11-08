class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        str = ""
        for s in strs:
            str += s + "라"
        return str[:len(str) - 1]
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("라")
        #strs = []
        #temp = ""
        #for c in s:
            #if c != '라':
                #temp += c
            #else:
                #strs.append(temp)
                #temp = ""
        #return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))