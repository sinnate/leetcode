class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        nmap : []  =[0]*10001
        total: int = 0
        best : int = 0
        left : int = 0

        for right in nums :
            nmap[right] +=1
            total += right
            while nmap[right] > 1 :
                nmap[nums[left]] -= 1
                total -=nums[left]
                left += 1
            best = max(best,total)
        return best