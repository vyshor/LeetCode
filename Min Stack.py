class MinStack:

    def __init__(self):
        self.dp = []
        self.min = None
        self.min_idx = None
        self.pt = []

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
            self.min_idx = 0
            self.pt.append(-1)

        elif self.min >= val:
            self.pt.append(self.min_idx)
            self.min_idx = len(self.pt) - 1
            self.min = val

        else:
            self.pt.append(-1)

        self.dp.append(val)

    def pop(self) -> None:
        nxt_min_idx = self.pt.pop()
        self.dp.pop()
        if nxt_min_idx != -1:
            self.min = self.dp[nxt_min_idx]
            self.min_idx = nxt_min_idx
        if len(self.dp) == 0:
            self.min = None

    def top(self) -> int:
        return self.dp[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()