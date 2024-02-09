class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = []
        n = len(words)
        counter = [0] * 26
        c_counter = []

        for c in letters:
            j = ord(c) - 97
            counter[j] += 1

        for word in words:
            val = 0
            char_count = [0] * 26
            for c in word:
                j = ord(c) - 97
                val += score[j]
                char_count[j] += 1

            scores.append(val)
            c_counter.append(char_count)

        maxx = 0
        total = 0
        chars = [0] * 26

        def getScore(i):
            nonlocal maxx, chars, total

            if i == n:
                maxx = max(maxx, total)
                return

            word_counter = c_counter[i]
            new_counter = [0] * 26
            invalid = False

            for j in range(26):
                new_counter[j] = word_counter[j] + chars[j]
                if new_counter[j] > counter[j]:
                    invalid = True
                    break

            if not invalid:
                old_counter = list(chars)
                chars = new_counter
                total += scores[i]
                getScore(i + 1)
                total -= scores[i]
                chars = old_counter

            getScore(i + 1)

        getScore(0)
        return maxx
