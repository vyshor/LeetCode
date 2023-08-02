class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1) + 1, len(s2) + 1
        m = [[0] * n2 for _ in range(n1)]

        # s1 being the vertical
        # s2 being horizontal

        # Base case
        for i in range(1, n1):
            m[i][0] = m[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n2):
            m[0][j] = m[0][j - 1] + ord(s2[j - 1])

        for i in range(1, n1):
            for j in range(1, n2):
                if s1[i - 1] != s2[j - 1]:
                    # 1st Cost = vertical above (which is cost to remove all the characters in s2 + s1)
                    # + cost of removing current char in s1
                    # 2nd Cost = horizontal left (which is cost to remove all the characters in s1 + s2)
                    # + cost of removing current char in s2

                    m[i][j] = min(m[i - 1][j] + ord(s1[i - 1]), m[i][j - 1] + ord(s2[j - 1]))
                else:
                    m[i][j] = m[i - 1][j - 1]
        return m[-1][-1]
