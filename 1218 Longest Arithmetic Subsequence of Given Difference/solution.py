class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        Result : int = 0
        leng = {}

        for i in arr :
            leng[i] = leng.get(i - difference,0) + 1
            Result = max(Result,leng[i])
        
        return Result