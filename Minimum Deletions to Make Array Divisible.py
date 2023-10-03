class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def hcf(i, j):
            while i != 0:
                i, j = j % i, i
            return j

        if 1 in nums:
            return 0

        factor = numsDivide[0]
        for num in numsDivide:
            factor = hcf(factor, num)

        if factor == 1:
            return -1

        heapq.heapify(nums)
        visited = set()
        count = 0

        while nums:
            i = heapq.heappop(nums)

            if i in visited:
                count += 1
                continue

            if factor % i == 0:
                return count
            else:
                count += 1
                visited.add(i)

        return -1
