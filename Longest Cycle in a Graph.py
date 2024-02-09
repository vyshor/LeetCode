class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        longest = -1

        for i in range(n):
            if i in visited:
                continue

            dist = 0
            path = {}
            while True:
                i = edges[i]
                dist += 1

                # Found loop
                if i in path:
                    longest = max(longest, dist - path[i])
                    break

                # Not cycle, or explored
                if i == -1 or i in visited:
                    break

                visited.add(i)
                path[i] = dist

        return longest
