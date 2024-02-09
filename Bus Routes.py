class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        source_found, target_found = False, False
        for route in routes:
            all_stops = set(route)
            if source in all_stops:
                source_found = True

            if target in all_stops:
                target_found = True

        if not source_found or not target_found:
            return -1

        edges = {}
        for route in routes:
            all_stops = set(route)
            for stop in all_stops:
                if stop not in edges:
                    edges[stop] = set()
                for next_stop in all_stops:
                    if stop != next_stop:
                        edges[stop].add(next_stop)

        q = deque([(source, 0)])
        visited = {source}

        while q:
            i, count = q.popleft()
            next_stops = edges[i]
            for stop in next_stops:
                if stop == target:
                    return count + 1

                if stop not in visited:
                    visited.add(stop)
                    q.append((stop, count + 1))

        return -1
