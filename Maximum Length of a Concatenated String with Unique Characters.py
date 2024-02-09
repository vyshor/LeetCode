class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        seen = set()
        maxx = 0

        def recur(i):
            nonlocal maxx, seen, n
            if i == n:
                maxx = max(maxx, len(seen))
                return

            word = arr[i]
            word_set = set(word)
            is_unique = len(word) == len(word_set)

            if is_unique:
                for c in word:
                    if c in seen:
                        is_unique = False
                        break

            if is_unique:
                seen.update(word_set)
                recur(i + 1)
                seen -= word_set

            recur(i + 1)

        recur(0)
        return maxx
