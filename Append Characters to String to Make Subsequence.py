class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s1, t1 = 0, 0
        sn, tn = len(s), len(t)
        while t1 < tn:
            while s1 < sn:
                if s[s1] == t[t1]:
                    s1 += 1
                    t1 += 1
                    break
                else:
                    s1 += 1

            if s1 == sn:
                return tn - t1
        return 0
