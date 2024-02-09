class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if m < k or k > n:
            return 0

        MOD = 10 ** 9 + 7
        dp = {}

        def exploreCombination(i, max_val, remaining_cost):
            nonlocal dp, MOD
            if (i, max_val, remaining_cost) in dp:
                return dp[(i, max_val, remaining_cost)]

            if i == n:
                if remaining_cost == 0:
                    dp[(i, max_val, remaining_cost)] = 1
                    return 1
                else:
                    dp[(i, max_val, remaining_cost)] = 0
                    return 0

            pre_sum = 0
            for j in range(1, m + 1):
                if j > max_val:
                    if remaining_cost >= 1:
                        pre_sum += exploreCombination(i + 1, j, remaining_cost - 1)
                elif n - i >= remaining_cost >= 0:
                    pre_sum += exploreCombination(i + 1, max_val, remaining_cost)

            pre_sum %= MOD

            dp[(i, max_val, remaining_cost)] = pre_sum
            return pre_sum

        ans = exploreCombination(0, float('-inf'), k) % MOD
        # print(dp)

        return ans

