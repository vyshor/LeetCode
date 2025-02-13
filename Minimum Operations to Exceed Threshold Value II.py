class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            if num < k:
                arr.append(num)
        heapq.heapify(arr)
        n = len(arr)
        count = 0
        while n > 1:
            minn = heapq.heappop(arr)
            minn2 = heapq.heappop(arr)
            x = (minn << 1) + minn2
            if x < k:
                heapq.heappush(arr, x)
                n -= 1
            else:
                n -= 2
            count += 1
        return count + n
