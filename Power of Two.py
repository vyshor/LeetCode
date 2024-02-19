class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n-1) == 0 if n > 0 else False

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 0:
#             return False
#         single_one = 0
#         while n:
#             if n & single_one:
#                 return False
#             single_one |= n & 1
#             n >>= 1
#         return True
