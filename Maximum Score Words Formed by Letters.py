class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = []
        for word in words:
            total = 0
            counter = [0] * 26
            for c in word:
                total += score[ord(c) - 97]
                counter[ord(c) - 97] += 1
            scores.append((total, counter))

        def updateCounter(delta, target, minus=True):
            if minus:
                for i in range(26):
                    if target[i] < delta[i]:
                        return False

            for i in range(26):
                target[i] += delta[i] * (-1 if minus else 1)
            return True

        n = len(words)
        maxx = 0
        current_score = 0
        current_counter = [0] * 26
        for c in letters:
            current_counter[ord(c) - 97] += 1

        def explore(i):
            nonlocal n, scores, words, maxx, current_score
            if i == n:
                maxx = max(maxx, current_score)
                return

            explore(i + 1)

            prev_score = current_score
            canMinus = updateCounter(scores[i][1], current_counter)
            if canMinus:
                current_score += scores[i][0]
                explore(i + 1)
                current_score = prev_score
                updateCounter(scores[i][1], current_counter, False)

        explore(0)
        return maxx

# class Solution:
#     def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
#         scores = []
#         n = len(words)
#         counter = [0] * 26
#         c_counter = []
#
#         for c in letters:
#             j = ord(c) - 97
#             counter[j] += 1
#
#         for word in words:
#             val = 0
#             char_count = [0] * 26
#             for c in word:
#                 j = ord(c) - 97
#                 val += score[j]
#                 char_count[j] += 1
#
#             scores.append(val)
#             c_counter.append(char_count)
#
#         maxx = 0
#         total = 0
#         chars = [0] * 26
#
#         def getScore(i):
#             nonlocal maxx, chars, total
#
#             if i == n:
#                 maxx = max(maxx, total)
#                 return
#
#             word_counter = c_counter[i]
#             new_counter = [0] * 26
#             invalid = False
#
#             for j in range(26):
#                 new_counter[j] = word_counter[j] + chars[j]
#                 if new_counter[j] > counter[j]:
#                     invalid = True
#                     break
#
#             if not invalid:
#                 old_counter = list(chars)
#                 chars = new_counter
#                 total += scores[i]
#                 getScore(i + 1)
#                 total -= scores[i]
#                 chars = old_counter
#
#             getScore(i + 1)
#
#         getScore(0)
#         return maxx
