class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        deads = set(deadends)
        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            comb, count = q.popleft()
            new_combs = []
            for i in range(4):
                c = comb[i]
                new_c = str((int(c) + 1) % 10)
                new_combs.append(comb[:i] + new_c + comb[i + 1:])

                new_c = str((int(c) - 1) % 10)
                new_combs.append(comb[:i] + new_c + comb[i + 1:])

            for comb in new_combs:
                if comb == target:
                    return count + 1

                if comb not in visited and comb not in deads:
                    q.append((comb, count + 1))
                    visited.add(comb)

        return -1

