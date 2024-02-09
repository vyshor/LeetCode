class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            return

        i = bisect.bisect_left(self.intervals, [value, value])
        n = len(self.intervals)
        if i < n:
            if self.intervals[i][0] == value:
                return
            if i - 1 >= 0 and self.intervals[i - 1][1] + 1 >= value:
                self.intervals[i - 1][1] = max(self.intervals[i - 1][1], value)
                i = i - 1
            else:
                self.intervals.insert(i, [value, value])
        else:
            if self.intervals[-1][1] + 1 >= value:
                self.intervals[-1][1] = max(self.intervals[-1][1], value)
            else:
                self.intervals.insert(i, [value, value])

        # Merge intervals
        if i + 1 < len(self.intervals) and self.intervals[i][1] + 1 >= self.intervals[i + 1][0]:
            self.intervals[i] = [self.intervals[i][0], max(self.intervals[i][1], self.intervals[i + 1][1])]
            self.intervals.pop(i + 1)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
