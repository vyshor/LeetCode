class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        visited = set()
        minn = -1
        path = {}
        for (u, v) in edges:
            if u not in path:
                path[u] = set()
            if v not in path:
                path[v] = set()

            path[u].add(v)
            path[v].add(u)

        def calculateCost(cost):
            t = 0
            t2 = 0
            can_go = True
            while cost:
                t += time
                cost -= 1
                t2 += time

                while t2 >= change:
                    t2 -= change
                    can_go = not can_go

                if not can_go and cost > 0:
                    t += change - t2
                    t2 = 0
                    can_go = True
            return t

        q = deque([(0, 1)])
        while q:
            # print(q)
            cost, pos = q.popleft()
            if (pos, cost % 2) in visited:
                continue
            else:
                visited.add((pos, cost % 2))

            if pos == n:
                # print(cost, pos)
                if minn == -1:
                    minn = calculateCost(cost + 2)
                elif cost != minn:
                    return min(minn, calculateCost(cost))

            if pos in path:
                for target in path[pos]:
                    if (target, (cost + 1) % 2) in visited:
                        continue

                    q.append((cost + 1, target))
        return minn

