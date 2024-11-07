class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dp = []

        def countBits(num):
            nonlocal dp
            i = 0
            while num:
                if i == len(dp):
                    dp.append(0)
                dp[i] += num % 2
                i += 1
                num >>= 1

        for num in candidates:
            countBits(num)
        return max(dp)
