class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        visited = set()

        deletion = 0

        for count in counter.values():
            while count in visited and count > 0:
                count -= 1
                deletion += 1

            if count > 0:
                visited.add(count)

        return deletion
