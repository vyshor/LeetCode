class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        m = len(spaces)
        new_str = ""
        j = 0

        for i in range(n):
            if j < m and i >= spaces[j]:
                new_str += " "
                j += 1

            new_str += s[i]

        return new_str
