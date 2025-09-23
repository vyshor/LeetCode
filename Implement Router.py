class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.seen = set()
        self.dq = deque([])
        self.counter = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        v = (source, destination, timestamp)
        if v in self.seen:
            return False

        if len(self.dq) == self.limit:
            v2 = self.dq.popleft()
            self.seen.remove(v2)
            self.counter[v2[1]].popleft()

        self.seen.add(v)
        self.dq.append(v)
        if destination not in self.counter:
            self.counter[destination] = deque([timestamp])
        else:
            self.counter[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.dq) == 0:
            return []
        v = self.dq.popleft()
        self.seen.remove(v)
        self.counter[v[1]].popleft()
        return v

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.counter:
            return 0

        t = self.counter[destination]
        sidx = bisect.bisect_left(t, startTime)
        eidx = bisect.bisect_right(t, endTime)
        return eidx - sidx

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
