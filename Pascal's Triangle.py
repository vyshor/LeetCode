class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            ans = [[1], [1,1]]
            dp = [1]
            last_dp = ans[-1]

            for _ in range(3, numRows+1):
                for i in range(1, len(last_dp)):
                    dp.append(last_dp[i] + last_dp[i-1])
                dp.append(1)

                ans.append(dp)
                last_dp = dp
                dp = [1]

            return ans
