class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        counter = Counter(s1)
        start, end = 0, 0
        for i in range(n1):
            c = s2[i]
            if c in counter:
                counter[c] -= 1

        if not any(counter.values()):
            return True

        for i in range(n1, n2):
            c = s2[i]
            if c in counter:
                counter[c] -= 1

            c2 = s2[i - n1]
            if c2 in counter:
                counter[c2] += 1

            if not any(counter.values()):
                return True

        return False



