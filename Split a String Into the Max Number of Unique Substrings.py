class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        word = []
        count = 0
        maxx = 0

        def recur(i):
            nonlocal n, seen, count, word, maxx, s
            if i == n:
                if ''.join(word) not in seen:
                    # print(''.join(word), count, seen)
                    if count + 1 > maxx:
                        maxx = count + 1
                return

            word.append(s[i])
            recur(i + 1)
            word.pop()

            formed = ''.join(word)
            if formed and formed not in seen:
                old_word = list(word)
                seen.add(formed)
                count += 1
                word = [s[i]]

                recur(i + 1)

                word = old_word
                seen.remove(formed)
                count -= 1

        recur(0)
        return maxx
