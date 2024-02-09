class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rows = {}
        cols = {}
        dp = {}

        for i, stone in enumerate(stones):
            x, y = stone
            if x not in rows:
                rows[x] = [i]
                dp[i] = []
            else:
                dp[i] = list(rows[x])
                for r in rows[x]:
                    dp[r].append(i)
                rows[x].append(i)

            if y not in cols:
                cols[y] = [i]
            else:
                dp[i] += cols[y]
                for c in cols[y]:
                    dp[c].append(i)
                cols[y].append(i)

        visited = set()
        count = 0
        for i in range(n):
            if i in visited:
                continue
            else:
                count += 1

                q = [i]
                while q:
                    j = q.pop()
                    visited.add(j)
                    for k in dp[j]:
                        if k not in visited:
                            q.append(k)
                            visited.add(k)

        # print(rows)
        # print(cols)
        # print(dp)
        return n - count

