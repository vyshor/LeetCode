class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(corridor)
        seats = 0
        factor = 1
        count = 1

        for i in range(n):
            if corridor[i] == 'S':
                seats += 1

                if seats == 3:
                    count *= factor
                    factor = 1
                    seats = 1
            else:
                if seats == 2:
                    factor += 1

        if seats != 2:
            return 0

        return count % MOD

