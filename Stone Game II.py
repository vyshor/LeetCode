class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        n = len(piles)

        def maximise(i, turn, m):
            nonlocal n, piles
            if i == n:
                return 0

            if (i, turn, m) in dp:
                return dp[(i, turn, m)]

            maxx = float('-inf')
            summ = 0
            for j in range(m * 2):
                if i + j >= n:
                    break

                summ += piles[i + j]
                maxx = max(maxx, summ - maximise(i + j + 1, not turn, max(m, j + 1)))

            dp[(i, turn, m)] = maxx
            return maxx

        total = sum(piles)
        max_diff = maximise(0, True, 1)
        # print(dp)
        if max_diff > 0:
            return (total - max_diff) // 2 + max_diff
        return (total + max_diff) // 2

# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
#         dp = {}
#         dp2 = {}
#
#         def takePile(i, m, aliceTurn):
#             if i == n:
#                 return 0, 0
#
#             if aliceTurn:
#                 if (i, m) in dp:
#                     return dp[(i, m)]
#             else:
#                 if (i, m) in dp2:
#                     return dp2[(i, m)]
#
#             maxx = float('-inf')
#             alice_maxx = 0
#             prefix = 0
#             k = 1
#
#             for j in range(i, min(n, i + 2 * m)):
#                 prefix += piles[j]
#                 nett_sum, aliceSum = takePile(j + 1, max(m, k), not aliceTurn)
#                 if prefix - nett_sum > maxx:
#                     maxx = prefix - nett_sum
#                     alice_maxx = aliceSum + (prefix if aliceTurn else 0)
#                 k += 1
#
#             if aliceTurn:
#                 dp[(i, m)] = maxx, alice_maxx
#                 return dp[(i, m)]
#             else:
#                 dp2[(i, m)] = maxx, alice_maxx
#                 return dp2[(i, m)]
#
#         _, ans = takePile(0, 1, True)
#         # print(dp)
#         return ans
