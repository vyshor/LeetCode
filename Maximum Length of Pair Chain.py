class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        (minleft, maxright) = pairs[0]
        for pair in pairs:
            left, right = pair
            minleft = min(minleft, left)
            maxright = max(maxright, right)

        dp = [0] * (maxright - minleft + 3)

        pairs.sort()

        # print(pairs)

        longest = 0
        i = 1
        for pair in pairs:
            left, right = pair
            rightidx = right - minleft + 2
            leftidx = left - minleft + 2
            while i < leftidx:
                dp[i] = max(dp[i], dp[i - 1])
                i += 1
            dp[rightidx] = max(dp[left - minleft + 1] + 1, dp[leftidx - 1])
            longest = max(longest, dp[rightidx])
            # print(rightidx, left-minleft+1, rightidx-1)
            # print(dp)

        # print(dp)
        return longest
