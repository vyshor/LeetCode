class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        lps = [0] * n

        if n > 1:
            i, j = 0, 1
            while j < n:
                if needle[i] == needle[j]:
                    lps[j] = i + 1
                    i += 1
                    j += 1

                else:
                    if i > 0:
                        i = lps[i - 1]
                    else:
                        j += 1

        i, j = 0, 0
        while j < h:
            if haystack[j] == needle[i]:
                i += 1
                j += 1

                if i == n:
                    return j - i

            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    j += 1

        return -1
