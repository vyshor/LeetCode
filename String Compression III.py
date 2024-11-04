class Solution:
    def compressedString(self, word: str) -> str:
        ss = []
        prev = word[0]
        count = 0
        for c in word:
            if prev == c:
                count += 1
                if count == 9:
                    ss.append(str(count) + prev)
                    count = 0
            else:
                if prev != '' and count > 0:
                    ss.append(str(count) + prev)
                prev = c
                count = 1

        if prev != '' and count > 0:
            ss.append(str(count) + prev)
        return ''.join(ss)
