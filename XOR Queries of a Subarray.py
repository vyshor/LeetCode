class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorr = 0
        dp = [0]
        n = len(arr)
        for i in range(n):
            xorr ^= arr[i]
            dp.append(xorr)

        ans = []
        for (left, right) in queries:
            ans.append(dp[right + 1] ^ dp[left])
        return ans
