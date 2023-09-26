class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(t)
        for c in s:
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        return list(counter.keys())[0]
