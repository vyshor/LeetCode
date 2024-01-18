class Solution:
    def climbStairs(self, n: int) -> int:
        t_2, t_1 = 0, 1
        for i in range(n):
            t_2, t_1 = t_1, t_2+t_1
        return t_1

# import math as m
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         total = 0
#         a = 0
#         while n-a>=0:
#             total += int(m.factorial(n)/(m.factorial(a) * m.factorial(n-a)))
#             a += 1
#             n -= 1
#         return total

# Time: O(n^2) # Assuming factorial is O(n) # Otherwise O(n) if factorial calculation is O(1)
# Space: O(1)
# Runtime: 28 ms, faster than 55.29% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.