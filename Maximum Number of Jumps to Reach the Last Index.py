class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = sorted([(num, i) for i, num in enumerate(nums)])
        dp = [-1] * n
        dp[0] = 0

        for pos in range(n):
            if dp[pos] == -1:
                continue

            left_target = nums[pos] - target
            right_target = nums[pos] + target
            left = bisect.bisect_left(arr, (left_target, float('-inf')))
            right = bisect.bisect_right(arr, (right_target, float('inf')))
            for i in range(left, min(right, n)):
                _, j = arr[i]
                if j > pos:
                    dp[j] = max(dp[j], dp[pos] + 1)

        return dp[-1]
