class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        tc = len(classes)
        c = []
        full_passes = 0
        for p, t in classes:
            if p == t:
                full_passes += 1
            else:
                c.append(((p/t-(p+1)/(t+1)), t, p))

        heapq.heapify(c)
        i = extraStudents
        while i and c:
            # print(c)
            _, t, p = heapq.heappop(c)
            i -= 1
            p += 1
            t += 1
            heapq.heappush(c, ((p/t-(p+1)/(t+1)), t, p))

        summ = full_passes
        for (_, t, p) in c:
            summ += p/t
        return summ / tc
    