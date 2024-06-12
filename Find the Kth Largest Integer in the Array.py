class Node:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        if len(self.num) != len(other.num):
            return len(self.num) < len(other.num)

        return self.num < other.num


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        q = []
        for num in nums:
            heapq.heappush(q, Node(num))

            if len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q).num
