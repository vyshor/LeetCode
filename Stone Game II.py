class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        dp2 = {}

        def takePile(i, m, aliceTurn):
            if i == n:
                return 0, 0

            if aliceTurn:
                if (i, m) in dp:
                    return dp[(i, m)]
            else:
                if (i, m) in dp2:
                    return dp2[(i, m)]

            maxx = float('-inf')
            alice_maxx = 0
            prefix = 0
            k = 1

            for j in range(i, min(n, i + 2 * m)):
                prefix += piles[j]
                nett_sum, aliceSum = takePile(j + 1, max(m, k), not aliceTurn)
                if prefix - nett_sum > maxx:
                    maxx = prefix - nett_sum
                    alice_maxx = aliceSum + (prefix if aliceTurn else 0)
                k += 1

            if aliceTurn:
                dp[(i, m)] = maxx, alice_maxx
                return dp[(i, m)]
            else:
                dp2[(i, m)] = maxx, alice_maxx
                return dp2[(i, m)]

        _, ans = takePile(0, 1, True)
        # print(dp)
        return ans
