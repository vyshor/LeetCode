class Solution:
    def reinitializePermutation(self, n: int) -> int:
        count = 1
        i = n // 2
        while i != 1:
            if i % 2:
                i = (n + i - 1) // 2
            else:
                i = i // 2
            count += 1
        return count
