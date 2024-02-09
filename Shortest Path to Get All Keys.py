class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        k = 0

        q = deque([])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    q.append((i, j, 0, 0, 0, 0))
                    visited.add((i, j, 0, 0))
                elif grid[i][j].islower():
                    k += 1

        while q:
            # print(q)
            # print(visited)
            i, j, moves, key_state, lock_state, key_count = q.popleft()
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] != "#" and (x, y, key_state, lock_state) not in visited:
                    if grid[x][y] == "." or grid[x][y] == "@":
                        visited.add((x, y, key_state, lock_state))
                        q.append((x, y, moves + 1, key_state, lock_state, key_count))

                    elif grid[x][y].islower():
                        new_key_state = key_state
                        new_key_count = key_count
                        key_pos = ord(grid[x][y]) - 97
                        if (new_key_state >> key_pos) % 2 == 0:
                            new_key_state = key_state | (1 << key_pos)
                            new_key_count += 1
                            if new_key_count == k:
                                return moves + 1

                        visited.add((x, y, new_key_state, lock_state))
                        q.append((x, y, moves + 1, new_key_state, lock_state, new_key_count))

                    elif grid[x][y].isupper():
                        new_lock_state = lock_state
                        lock_pos = ord(grid[x][y]) - 65
                        if (key_state >> lock_pos) % 2:
                            new_lock_state = lock_state | (1 << (lock_pos))
                            visited.add((x, y, key_state, new_lock_state))
                            q.append((x, y, moves + 1, key_state, new_lock_state, key_count))

        return -1
