class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = {}
        ans_right = [0] * n
        count = {}
        for i in range(n):
            num = nums[i]
            if num in dp:
                ans_right[i] = ans_right[dp[num]] + (i - dp[num]) * count[num]
            dp[num] = i

            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        dp = {}
        count = {}
        ans_left = [0] * n

        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in dp:
                ans_left[i] = ans_left[dp[num]] + (dp[num] - i) * count[num]
            dp[num] = i

            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        ans = [ans_left[i] + ans_right[i] for i in range(n)]
        return ans
