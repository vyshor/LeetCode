class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.arr = []

    def seat(self) -> int:
        if len(self.arr) == 0:
            p = 0
        else:
            n = len(self.arr)
            max_dist = 0
            p = self.n - 1

            if self.arr[-1] != self.n - 1:
                max_dist = self.n - 1 - self.arr[-1]

            for i in range(n - 1, 0, -1):
                new_dist = (self.arr[i] - self.arr[i - 1]) // 2
                if new_dist >= max_dist:
                    max_dist = new_dist
                    p = self.arr[i - 1] + new_dist

            if self.arr[0] >= max_dist:
                p = 0

            # print(p, max_dist)
        bisect.insort_left(self.arr, p)
        # print(self.arr)
        return p

    def leave(self, p: int) -> None:
        i = bisect.bisect_left(self.arr, p)
        self.arr.pop(i)
        # print(self.arr)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)