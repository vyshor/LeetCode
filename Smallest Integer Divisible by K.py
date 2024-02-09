class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        else:
            i = 1
            count = 1
            while i % k != 0:
                i *= 10
                i += 1
                count += 1
            return count
