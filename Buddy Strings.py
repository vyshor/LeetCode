class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        def compare(a, b):
            n = len(a)
            diff = 0
            for i in range(n):
                if a[i] != b[i]:
                    diff += 1
            return diff

        return (s != goal or max(Counter(s).values()) > 1) and Counter(s) == Counter(goal) and compare(s, goal) <= 2
