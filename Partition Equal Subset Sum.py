class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2:
            return False
        target = summ // 2

        dp = [False] * (target + 1)
        dp[target] = True

        for key in nums:
            for i in range(key, target + 1):
                if dp[i]:
                    if key > i:
                        break

                    if i - key == 0:
                        return True

                    dp[i - key] = True

        return False

