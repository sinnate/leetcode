class Solution:
    def checkWord(self,word,dic) -> int:
        if len(word) != len(dic):
            return -1
        # Max edits are 2 
        Edits = sum(ch1 != ch2 for ch1, ch2 in zip(word, dic))
        if Edits <= 2 :
            return Edits
        return -1
        
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        #Let's start we need to return a List
        Result : List[str] = []
        for i in range (0,len(queries)):
            for j in range(0,len(dictionary)):
                if self.checkWord(queries[i],dictionary[j]) > -1:
                    Result.append(queries[i])
                    break

       

        return Result

    
