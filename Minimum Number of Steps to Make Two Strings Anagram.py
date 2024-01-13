class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        total = 0
        for c, count in counter_s.items():
            other_count = counter_t.get(c, 0)
            total += max(count - other_count, 0)
        return total
