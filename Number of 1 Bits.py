class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n % 2)
            n >>= 1
        return count

# from collections import Counter
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return Counter(str(bin(n))).get('1', 0)


# Runtime: 40 ms, faster than 13.70% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14.3 MB, less than 40.36% of Python3 online submissions for Number of 1 Bits.

# Time: O(n)
# Space: O(1)