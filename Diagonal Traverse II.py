class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n, m = len(nums), len(nums[0])
        dp = []
        i = 0
        for arr in nums:
            for j, num in enumerate(arr):
                if i+j >= len(dp):
                    dp.append(deque([num]))
                else:
                    dp[i+j].appendleft(num)
            i += 1

        ans = []
        for arr in dp:
            for num in arr:
                ans.append(num)

        return ans
