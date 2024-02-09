class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [(0, i) for i in range(n)]
        dp = set()
        for c0, c1 in roads:
            if c1 < c0:
                c0, c1 = c1, c0

            degrees[c0] = (degrees[c0][0] - 1, degrees[c0][1])
            degrees[c1] = (degrees[c1][0] - 1, degrees[c1][1])
            dp.add((c0, c1))

        heapq.heapify(degrees)
        max1, max2 = [], []

        max_rank, max_idx = heapq.heappop(degrees)
        max1.append((max_rank, max_idx))
        while degrees and degrees[0][0] == max_rank:
            max1.append(heapq.heappop(degrees))

        if degrees:
            max_rank2, max_idx2 = heapq.heappop(degrees)
            max2.append((max_rank2, max_idx2))
            while degrees and degrees[0][0] == max_rank2:
                max2.append(heapq.heappop(degrees))

        # print(max1)
        # print(max2)
        # print(dp)

        if len(max1) >= 2:
            for i in range(len(max1)):
                for j in range(i + 1, len(max1)):
                    if (max1[i][1], max1[j][1]) not in dp:
                        return max_rank * -2
            return max_rank * -2 - 1

        else:
            for i in range(len(max2)):
                if ((max_idx, max2[i][1]) if max_idx < max2[i][1] else (max2[i][1], max_idx)) not in dp:
                    return (max_rank + max2[i][0]) * -1
            else:
                return (max_rank + max2[i][0]) * -1 - 1
