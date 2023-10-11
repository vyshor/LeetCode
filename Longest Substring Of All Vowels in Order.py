class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        prev = word[0]
        unique = 1
        maxx = 0
        left, right = 0, 1
        while right < n:
            if word[right] < prev:
                left = right
                unique = 1
            else:
                if word[right] != prev:
                    unique += 1
                if unique == 5:
                    maxx = max(maxx, right - left + 1)

            prev = word[right]
            right += 1

        return maxx
