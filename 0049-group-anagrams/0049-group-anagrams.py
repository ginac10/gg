class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)#{}
        for s in strs:
            temp = [0]*26 #
            for letter in s:
                index =  ord(letter) - ord("a") # You must make "a" to int AND subtract it
                                                # In Python, NOT int("a"), but ord("a")
                temp[index] = temp[index]+1
                ##temp = temp[:index] + str(int(temp[index])+1) + temp[index+1:] # Str doesn't support item reassignment
            temp  = '#'.join(str(x) for x in temp) ## https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string ## Need token to split the numbers
            
            dic[temp].append(s) 
                # No need to do this
                    #if temp in dic:
                    #    dic[temp].append(s) #
                    #else:
                    #    dic[temp] = [s]
        
        return dic.values() # This cleanly returns the result in []
                    #result = []
                    #for v in dic.values():
                    #    result.append(v)
                    #return result