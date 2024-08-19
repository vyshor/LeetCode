class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        i = 2
        while n > 1 and i <= n:
            if n % i == 0:
                steps += i
                n //= i
                continue
            else:
                i += 1
        if n != 1:
            return steps + n
        return steps


