class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        count = 0
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    count += 1
                else:
                    count -= 1

        return count > 0
