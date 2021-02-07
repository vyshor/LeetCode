class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bi = ''
        for i in range(1, n+1):
            bi += bin(i)[2:]
        return int(bi, 2) % (10 ** 9 + 7)


# Runtime: 1384 ms, faster than 73.42% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# Memory Usage: 16.3 MB, less than 30.83% of Python3 online submissions for Concatenation of Consecutive Binary Numbers

# Time: O(n)
# Space: O(n)