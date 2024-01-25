class SmallestInfiniteSet:

    def __init__(self):
        self.q = [(1, True)]

    def popSmallest(self) -> int:
        # print("Pop", self.q)
        num, is_last = heapq.heappop(self.q)
        while self.q and self.q[0][0] == num:
            num, is_last = heapq.heappop(self.q)

        if is_last:
            heapq.heappush(self.q, (num + 1, True))

        return num

    def addBack(self, num: int) -> None:
        heapq.heappush(self.q, (num, False))
        # print("Push", self.q)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)