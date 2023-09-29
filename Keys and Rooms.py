class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = {0}

        q = [0]
        while q:
            i = q.pop()
            keys = rooms[i]

            for key in keys:
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        return len(visited) == n
