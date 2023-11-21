class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        last_end = 0
        maxx = 0
        hardest = 0
        for (_id, end) in logs:
            t = end - last_end
            if t == maxx:
                hardest = min(hardest, _id)
            elif t > maxx:
                maxx = t
                hardest = _id
            last_end = end

        return hardest
