#
# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         max_cap = sum(batteries)
#         batteries.sort()
#         if n==1 and len(batteries) <= 1:
#             return batteries[0]
#                # Using the Pythonic way of the last Array In some text case will throw an error as list index out of range 
#         while batteries[-1] >= max_cap // n :
#             max_cap -= batteries.pop()
#             n-=1
#       
#         return max_cap // n

# Oh well let do binary search 

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n==1 and len(batteries) <= 1:
            return batteries[0]
        def check(n, batteries, mid):
            return sum(min(b, mid) for b in batteries) >= n*x
        # Binary Search
        left, right = min(batteries), sum(batteries)//n
        while left <= right:
            mid = left + (right-left)//2
            if not check(n, batteries, mid):
                right = mid-1
            else:
                left = mid+1
        return right
