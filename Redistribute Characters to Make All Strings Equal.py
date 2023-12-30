class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = {}
        for word in words:
            for c in word:
                if c not in counter:
                    counter[c] = 1
                else:
                    counter[c] += 1

        for c, count in counter.items():
            if count % n != 0:
                return False

        return True
