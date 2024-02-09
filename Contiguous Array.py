class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        stack1, stack2 = [], []
        n = len(nums)
        dp = [0] * n

        for i, num in enumerate(nums):
            if num:
                if stack2:
                    start = stack2.pop()
                    dp[i] = i - start + 1
                    if start - 1 >= 0:
                        dp[i] += dp[start-1]
                stack1.append(i)
            else:
                if stack1:
                    start = stack1.pop()
                    dp[i] = i - start + 1
                    if start - 1 >= 0:
                        dp[i] += dp[start-1]
                stack2.append(i)

        return max(dp)
