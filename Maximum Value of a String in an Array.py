class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxx = float('-inf')
        for s in strs:
            is_int = True
            for c in s:
                if c.isalpha():
                    is_int = False
                    break
            if is_int:
                maxx = max(maxx, int(s))
            else:
                maxx = max(maxx, len(s))

        return maxx
