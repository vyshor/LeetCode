class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        window = 0
        window_size = 2 * k + 1

        for _ in range(min(k, n // 2)):
            ans.append(-1)

        for i in range(min(n, 2 * k)):
            window += nums[i]

        for i in range(2 * k, n):
            window += nums[i]
            ans.append(window // window_size)
            window -= nums[i - 2 * k]

        while len(ans) < n:
            ans.append(-1)

        return ans
