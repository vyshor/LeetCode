class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        score = 0
        q = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(q)

        while q:
            num, i = heapq.heappop(q)
            if i in marked:
                continue

            score += num
            marked.add(i)
            marked.add(i - 1)
            marked.add(i + 1)

        return score
