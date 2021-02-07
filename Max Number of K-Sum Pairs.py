class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        total_op = 0
        dp = {}
        ls = []
        for num in nums:
            if not dp.get(num):
                dp[num] = 1
                ls.append(num)
            else:
                dp[num] += 1
        ls.sort()
        for num in ls:
            other = k - num
            if other < num:
                break
            if dp.get(other):
                if num == other:
                    total_op += dp[num] // 2
                else:
                    total_op += min(dp[other], dp[num])

        return total_op

# Runtime: 664 ms, faster than 77.38% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.4 MB, less than 40.53% of Python3 online submissions for Max Number of K-Sum Pairs.

# Time: O(nlgn)
# Space: O(n)