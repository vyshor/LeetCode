class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        dp = {}
        dp[0] = [n]
        summ = 0
        for i in range(n - 1, -1, -1):
            summ += nums[i]
            summ %= p
            if summ not in dp:
                dp[summ] = [i]
            else:
                dp[summ].append(i)

        minn = dp[0][-1]
        summ = 0
        # print(dp)
        for i in range(n):
            summ += nums[i]
            summ %= p
            complement = (p - summ) % p
            while complement in dp and dp[complement] and dp[complement][-1] <= i:
                dp[complement].pop()

            if complement in dp and dp[complement]:
                minn = min(minn, dp[complement][-1] - i - 1)

        if minn == n:
            return -1
        return minn
