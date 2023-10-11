class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = {}
        count = 0
        for num in nums:
            rev = int(str(num)[::-1])
            diff = num - rev
            if diff in dp:
                count += dp[diff]
                dp[diff] += 1
            else:
                dp[diff] = 1

        return count % MOD
