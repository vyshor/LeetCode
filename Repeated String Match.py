class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)

        lps = [0] * nb
        if nb != 1:
            i, j = 0, 1
            while j < nb:
                if b[i] == b[j]:
                    lps[j] = i + 1
                    j += 1
                    i += 1
                else:
                    if i != 0:
                        i = lps[i-1]
                    else:
                        j += 1

        def checkSubstr(word):
            n = len(word)
            i, j = 0, 0
            while i < n:
                if word[i] == b[j]:
                    i += 1
                    j += 1

                    if j == nb:
                        return True
                else:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1


        count = (nb // na)
        s = a * count
        for i in range(3):
            if checkSubstr(s):
                return count
            else:
                count += 1
                s += a
        return -1
