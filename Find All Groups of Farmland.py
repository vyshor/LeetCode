class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        ans = []
        jumps = {}

        i = 0
        while i < n:
            j = 0
            while j < m:
                if land[i][j]:
                    if (i, j) in jumps:
                        j = jumps[(i, j)]
                        continue
                    else:
                        x = i
                        y = j
                        while y+1 < m and land[x][y+1]:
                            y += 1

                        while x+1 < n and land[x+1][y]:
                            x += 1
                        ans.append([i, j, x, y])
                        for k in range(i+1, x+1):
                            jumps[(k, j)] = y+1
                        j = y
                j += 1
            i += 1
        return ans
