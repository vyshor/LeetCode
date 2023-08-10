class LRUCache:

    def __init__(self, capacity: int):
        self.dp = {}
        self.keys = {}
        self.capacity = capacity
        self.least_used = deque()
        self.rolling_key = 0

    def get(self, key: int) -> int:
        if key in self.dp:
            self.keys[key] = self.rolling_key
            self.least_used.append((self.rolling_key, key))
            self.rolling_key += 1
            return self.dp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dp:
            self.dp[key] = value
            self.keys[key] = self.rolling_key
            self.least_used.append((self.rolling_key, key))
            self.rolling_key += 1
            return

        while len(self.dp) >= self.capacity:
            rolling_key, old_key = self.least_used.popleft()
            latest_rolling = self.keys[old_key]
            if latest_rolling != rolling_key:
                continue
            del self.dp[old_key]
            del self.keys[old_key]

        self.dp[key] = value
        self.keys[key] = self.rolling_key
        self.least_used.append((self.rolling_key, key))
        self.rolling_key += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
