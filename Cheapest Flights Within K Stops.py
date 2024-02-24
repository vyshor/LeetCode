class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {}
        for (_from, _to, _price) in flights:
            if _from not in edges:
                edges[_from] = [(_to, _price)]
            else:
                edges[_from].append((_to, _price))

        dp = {}
        q = [(0, src, k + 1)]
        while q:
            cost, pos, stops = heapq.heappop(q)
            if pos in dp:
                skip_current_step = False
                for current_cost, remaining_k in dp[pos]:
                    if current_cost <= cost and remaining_k >= stops:
                        skip_current_step = True
                        continue

                if skip_current_step:
                    continue
            else:
                dp[pos] = []

            dp[pos].append((cost, stops))

            if pos == dst:
                return cost

            if pos not in edges or stops <= 0:
                continue

            new_stops = stops - 1
            for _to, _price in edges[pos]:
                heapq.heappush(q, (cost + _price, _to, new_stops))

        return -1
