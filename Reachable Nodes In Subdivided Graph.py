class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        dp = {}
        dist = {}
        count = 1

        for edge in edges:
            fro, to, w = edge

            dist[(fro, to)] = w
            if fro not in dp:
                dp[fro] = [(w + 1, fro, to)]
            else:
                dp[fro].append((w + 1, fro, to))

            if to not in dp:
                dp[to] = [(w + 1, to, fro)]
            else:
                dp[to].append((w + 1, to, fro))

        if 0 not in dp:
            return count

        visited_nodes = {0: 0}
        visited_edges = set()
        dist_edges = {}

        q = []
        for edge in dp[0]:
            w, fro, to = edge
            if w > maxMoves:
                heapq.heappush(q, (maxMoves, fro, to, 0))
            else:
                heapq.heappush(q, (w, fro, to, 1))

        while q:
            # print("Queue:", q)
            # print("Visited Nodes:", visited_nodes)
            # print("Visited Edges:", visited_edges)
            # print("Count:", count)
            # print("===============")

            w, fro, to, reachNode = heapq.heappop(q)

            if (fro, to) in visited_edges:
                continue

            # If unable to reach node
            if not reachNode:
                reach_dist = w - visited_nodes[fro]
                if (to, fro) in dist_edges:
                    prev_reach = dist_edges[(to, fro)]
                    total_reach = prev_reach + reach_dist
                    visited_edges.add((fro, to))

                    # print("Fro:", fro, "To:", to)
                    # print("Total Reach:", total_reach)
                    # print("Prev Reach:", prev_reach)

                    if (fro, to) in dist:
                        count += min(dist[(fro, to)], total_reach) - prev_reach
                    else:
                        count += min(dist[(to, fro)], total_reach) - prev_reach
                else:
                    dist_edges[(fro, to)] = reach_dist
                    visited_edges.add((fro, to))
                    count += reach_dist
                continue

            # If can reach the node
            if to not in visited_nodes:
                visited_nodes[to] = w
            else:
                w -= 1

            visited_edges.add((fro, to))
            visited_edges.add((to, fro))
            count += w - visited_nodes[fro]

            for edge in dp[to]:
                w2, fro2, to2 = edge
                if (fro2, to2) not in visited_edges:
                    if visited_nodes[to] + w2 >= maxMoves:
                        # If I cannot reach the next node
                        heapq.heappush(q, (maxMoves, fro2, to2, 0))
                    else:
                        # If I can reach the next node
                        heapq.heappush(q, (visited_nodes[to] + w2, fro2, to2, 1))

        return count





