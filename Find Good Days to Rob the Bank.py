class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))

        if n <= 2 * time:
            return []

        ans = []
        lte = [security[i] > security[i + 1] for i in range(n - 1)]
        gte = [security[i] < security[i + 1] for i in range(n - 1)]

        # print(lte)
        # print(gte)

        gteq = deque(gte[0:time])
        lteq = deque(lte[time:2 * time])

        gte_count = sum(gteq)
        lte_count = sum(lteq)

        for i in range(time, n - time - 1):
            if gte_count == 0 and lte_count == 0:
                ans.append(i)

            gte_count += gte[i] - gteq.popleft()
            lte_count += lte[i + time] - lteq.popleft()
            gteq.append(gte[i])
            lteq.append(lte[i + time])

        if gte_count == 0 and lte_count == 0:
            ans.append(n - time - 1)

        return ans

