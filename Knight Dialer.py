class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        MOD = 10 ** 9 + 7
        next_steps = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }
        dp = {}

        def jump(pos, steps):
            if steps == 0:
                return 1
            if (pos, steps) in dp:
                return dp[(pos, steps)]
            ans = 0
            for next_pos in next_steps[pos]:
                ans += jump(next_pos, steps - 1)
            ans %= MOD
            dp[(pos, steps)] = ans
            return ans

        steps = 0
        for starting_pos in next_steps.keys():
            steps += jump(starting_pos, n - 1)
        return steps % MOD

