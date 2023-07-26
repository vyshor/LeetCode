class Solution:
    dp = {
        1: set(["()"]),
        2: set(["()()",  "(())"]),
    }

    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.dp:
            return self.dp[n]
        for i in range(3, n+1):
            self.getPaths(i)
        return list(self.dp[n])

    def getPaths(self, n: int):
        subPaths = self.dp[n-1]
        newPaths = []
        for subPath in subPaths:
            newPaths += ["()" + subPath, "(" + subPath + ")", subPath + "()"]

        for i in range(n-2, 1, -1):
            i2 = n - i

            subSubPaths = self.dp[i]
            subSubPaths2 = self.dp[i2]
            for subSubPath in subSubPaths:
                for subSubPath2 in subSubPaths2:
                    newPaths += [subSubPath + subSubPath2, subSubPath2 + subSubPath]

        self.dp[n] = set(newPaths)
