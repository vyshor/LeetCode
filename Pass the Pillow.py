class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn = 2 * n - 2
        time %= turn
        return 2 * n - time - 1 if time >= n else time + 1
