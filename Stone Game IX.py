class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones = [stone % 3 for stone in stones]

        # print(stones)
        counter = Counter(stones)

        # print(counter)

        def willWin(aliceTurn, flipper, loser, hasPass):
            # print(aliceTurn, flipper, loser, hasPass)

            if flipper <= 0 and loser <= 0:
                return not aliceTurn

            if flipper <= 0 and loser >= 1:
                return hasPass

            return not willWin(not aliceTurn, loser, flipper - 1, hasPass)

        hasPass = (counter.get(0, 0) % 2) == 1
        ones, twos = counter.get(1, 0), counter.get(2, 0)

        if ones and not willWin(False, ones - 1, twos, hasPass):
            return True
        if twos and not willWin(False, twos - 1, ones, hasPass):
            return True
        return False

# 1 + 1 -> 2
# 1 + 2 -> Lose
# 1 + 3 -> 1

# 2 + 1 -> Lose
# 2 + 2 -> 1
# 2 + 3 -> 2

# 2 (A) - 2 (B) - 1 (A) - 2 (B) - Pass (A)
#