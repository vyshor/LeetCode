class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        dp = {}
        for i in range(m):
            for i2 in range(n):
                if mat[i][i2] == 0:
                    dp[(i, i2)] = 0
                else:
                    q.append((i, i2))

        q.append((-1,-1))
        update_dp = {}
        while len(q) > 1:
            x, y = q.popleft()

            if (x, y) == (-1, -1):
                dp.update(update_dp)
                update_dp = {}
                q.append((-1, -1))
                continue

            found = False
            smallestDistance = 999
            for x1, y1 in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
                if (x1, y1) in dp:
                    smallestDistance = min(dp[(x1, y1)]+1, smallestDistance)
                    found = True
            if not found:
                q.append((x,y))
            else:
                update_dp[(x,y)] = smallestDistance


        dp.update(update_dp)
        for i in range(m):
            for i2 in range(n):
                mat[i][i2] = dp[(i, i2)]
        return mat

# Time: O(n x m x maxheight)
# Space: O(n x m)

# Runtime: 636 ms, faster than 76.98% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.2 MB, less than 65.64% of Python3 online submissions for 01 Matrix.
