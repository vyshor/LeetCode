class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0

        q = deque([(0, 0, False)])
        forbidden = set(forbidden)
        max_forbidden = max(forbidden)
        visited = set()

        while q:
            pos, move, jumped_prev = q.popleft()
            if not jumped_prev:
                new_pos = pos - b
                if new_pos == x:
                    return move + 1
                elif new_pos > 0 and new_pos not in forbidden and new_pos not in visited:
                    visited.add(new_pos)
                    q.append((new_pos, move + 1, True))

            if a >= b and pos > x:
                continue

            if pos > max(max_forbidden + a + b, x + b):
                continue

            new_pos = pos + a
            if new_pos == x:
                return move + 1
            if new_pos not in forbidden and new_pos not in visited:
                visited.add(new_pos)
                q.append((new_pos, move + 1, False))

        return -1
