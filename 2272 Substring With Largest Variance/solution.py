class Solution:
    def largestVariance(self, s: str) -> int:
        # Let's start we need something to keep track of every letter
        count = collections.Counter(s)
        Result : int = 0
        
        for char1, char2 in itertools.permutations(count,2):
            # We have number of letter ie 'a' and we will loop through to see if there is any variance
            char1_count = count[char1]
            char2_count = count[char2]

            differance = 0

            last_char1 = last_char2 = False

            for char in s:
                if char not in (char1,char2):
                    continue
                if differance < 0:
                    if not char1_count :
                        break
                    if not char2_count :
                        Result = max(Result, differance + char1_count)
                        break
                    last_char1 = last_char2 = False
                    differance = 0
                
                if char == char1:
                    last_char1 = True
                    char1_count -= 1
                    differance +=1
                if char == char2:
                    last_char2 = True
                    char2_count -= 1
                    differance -=1
                if last_char1 and last_char2:
                    Result = max(Result,differance)
        return Result
