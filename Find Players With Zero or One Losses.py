class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        for (winner, loser) in matches:
            if winner not in count:
                count[winner] = 0

            if loser not in count:
                count[loser] = 1
            else:
                count[loser] += 1

        zero, one = [], []
        for name, i in count.items():
            if i == 0:
                zero.append(name)
            elif i == 1:
                one.append(name)

        one.sort()
        zero.sort()

        return [zero, one]
