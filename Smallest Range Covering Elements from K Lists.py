class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        q = []
        maxx = nums[0][0]
        for i, arr in enumerate(nums):
            maxx = max(maxx, arr[0])
            q.append((arr[0], i, 0))

        heapq.heapify(q)
        minn = maxx - q[0][0]
        ans = [q[0][0], maxx]

        while True:
            if maxx - q[0][0] < minn:
                minn = maxx - q[0][0]
                ans = [q[0][0], maxx]

            _, i, j = heapq.heappop(q)
            if j + 1 == len(nums[i]):
                return ans

            heapq.heappush(q, (nums[i][j + 1], i, j + 1))
            maxx = max(maxx, nums[i][j + 1])


