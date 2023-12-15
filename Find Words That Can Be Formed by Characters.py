class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        summ = 0
        for word in words:
            required = Counter(word)
            can_build = True
            for c, count in required.items():
                if c not in counter or counter[c] < count:
                    can_build = False
                    break
            if can_build:
                summ += len(word)

        return summ
