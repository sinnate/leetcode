class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        CountMax = 1 << 16
        
        Result = 0
        count = [0] * CountMax

        for i in nums:
            for j in nums :
                count[i&j] += 1
        
        for num in nums :
            for k in range(CountMax):
                if (num & k) == 0:
                 Result += count[k]
    
        return Result
