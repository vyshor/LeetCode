class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = {}

        for c in licensePlate:
            c = c.lower()
            if c.isalpha():
                if c not in counter:
                    counter[c] = 1
                else:
                    counter[c] += 1

        count = float('inf')
        ans = ""
        for word in words:
            new_counter = dict(counter)
            matching = len(new_counter)
            for c in word:
                if c in new_counter:
                    new_counter[c] -= 1
                    if new_counter[c] == 0:
                        matching -= 1

            if matching == 0:
                if len(word) < count:
                    ans = word
                    count = len(word)

        return ans
