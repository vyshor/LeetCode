class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        ans = [['.'] * n for _ in range(m)]
        for i in range(n):
            k = m-1
            for j in range(m-1, -1, -1):
                if box[i][j] == "*":
                    ans[j][n-1-i] = "*"
                    k = j-1
                elif box[i][j] == "#":
                    ans[k][n-1-i] = "#"
                    k -= 1
        return ans
