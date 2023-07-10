from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        Result: int = 1
        MinD = deque()
        MaxD = deque()

        Left = 0
        for Right in range(len(nums)):
            while MinD and MinD[-1] > nums[Right]:
                MinD.pop()
            MinD.append(nums[Right])

            while MaxD and MaxD[-1] < nums[Right]:
                MaxD.pop()
            MaxD.append(nums[Right])

            while MaxD[0] - MinD[0] > limit:
                if MinD[0] == nums[Left]:
                    MinD.popleft()
                if MaxD[0] == nums[Left]:
                    MaxD.popleft()
                Left += 1
            Result = max(Result, Right - Left + 1)
        return Result
