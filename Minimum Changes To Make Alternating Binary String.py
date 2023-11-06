class Solution:
    def minOperations(self, s: str) -> int:
        count_1, count_0 = 0, 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == "0":
                    count_1 += 1
                else:
                    count_0 += 1
            else:
                if c == "1":
                    count_1 += 1
                else:
                    count_0 += 1
        return min(count_0, count_1)
