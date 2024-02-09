class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        twice = 2 * n
        i = int(math.sqrt(twice)) - 1
        count = 0

        while i * (i + 1) <= twice:
            count = max(count, i)
            i += 1

        return count

# 1 = 1 group
# 3 = 2 groups
# 6 = 3 groups
# 10 = 4 groups
# 10 = 4*5 // 2
# 20 = 4*5
# sqrt(20) = 4.

# n = x*(x+1) // 2
# 2n = x*(x+1) <= x^2
# Find x
