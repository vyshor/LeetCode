class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            prev, current = 0, 1
            for _ in range(n-1):
                prev, current = current, prev+current
            return current
