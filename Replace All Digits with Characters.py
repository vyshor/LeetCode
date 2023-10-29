class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = []
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if i + 1 >= n:
                arr += c
                break

            d = int(s[i + 1])
            arr += c + chr(ord(c) + d)
            i += 2
        return ''.join(arr)
