class Solution:
    def minTimeToType(self, word: str) -> int:
        i = 0
        t = 0
        for c in word:
            new_pos = ord(c) - 97
            t += min((i-new_pos+26) % 26, (new_pos-i+26) % 26) + 1
            i = new_pos
        return t
