class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] != self.snap_id:
            self.history[index].append((self.snap_id, val))
        else:
            self.history[index][-1] = (self.snap_id, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.history[index], (snap_id, ))
        # print(self.history[index], i)
        if i == len(self.history[index]):
            return self.history[index][-1][1]
        elif self.history[index][i][0] == snap_id:
            return self.history[index][i][1]
        else:
            return self.history[index][i-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
