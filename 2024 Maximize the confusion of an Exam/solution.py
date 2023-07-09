class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Max consectuvie for any option is 3
        # we will need sliding window
        # we also need to trakc the max frequency of T or F
        # we will use a dictionary for anwserKey we already know that answerkey return 'T' of 'F'
        count = {
            'T':0,
            'F':0
        }
        max_freq : int = 0
        j : int = 0

        for i in range(len(answerKey)):
            # This way it more simpler to incremante T and F
            count[answerKey[i]] +=1
            max_freq = max(max_freq,count[answerKey[i]])
            if i - j + 1 > max_freq + k:
                count[answerKey[j]] -= 1
                j +=1
        
        return len(answerKey)-j
            