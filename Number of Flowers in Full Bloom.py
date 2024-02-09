class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(people)
        m = len(flowers)
        ppl = [(person, i) for i, person in enumerate(people)]
        ans = [0] * n

        flowers.sort()
        ppl.sort()

        j = 0
        q = []
        count = 0
        for t, i in ppl:
            while j < m and flowers[j][0] <= t:
                count += 1
                heapq.heappush(q, flowers[j][1])
                j += 1

            while q and q[0] < t:
                heapq.heappop(q)
                count -= 1

            ans[i] = count

        return ans
