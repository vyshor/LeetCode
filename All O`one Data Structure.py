class AllOne:

    def __init__(self):
        self.key_to_count = {}
        self.count_to_keys = {}
        self.max_count = -1
        self.min_count = -1

    def inc(self, key: str) -> None:
        if key not in self.key_to_count:
            self.key_to_count[key] = 0

        prev_count = self.key_to_count[key]
        new_count = prev_count + 1
        self.key_to_count[key] = new_count

        if new_count not in self.count_to_keys:
            self.count_to_keys[new_count] = set()
        if prev_count not in self.count_to_keys:
            self.count_to_keys[prev_count] = set()

        self.count_to_keys[new_count].add(key)
        if key in self.count_to_keys[prev_count]:
            self.count_to_keys[prev_count].remove(key)

        if self.min_count == prev_count:
            if len(self.count_to_keys[prev_count]) == 0:
                self.min_count = new_count

        if new_count > self.max_count:
            self.max_count = new_count

        if self.min_count == -1 or new_count < self.min_count:
            self.min_count = new_count

    def dec(self, key: str) -> None:
        prev_count = self.key_to_count[key]
        new_count = prev_count - 1
        self.key_to_count[key] = new_count

        if new_count not in self.count_to_keys:
            self.count_to_keys[new_count] = set()
        if prev_count not in self.count_to_keys:
            self.count_to_keys[prev_count] = set()

        self.count_to_keys[new_count].add(key)
        if key in self.count_to_keys[prev_count]:
            self.count_to_keys[prev_count].remove(key)

        if self.max_count == prev_count:
            if len(self.count_to_keys[prev_count]) == 0:
                self.max_count = new_count

        if new_count == 0:
            del self.key_to_count[key]
            # Find the new min_count
            if self.min_count == prev_count and len(self.key_to_count) != 0:
                valid_counts = []
                for count, keys in self.count_to_keys.items():
                    if len(keys) > 0 and count != 0:
                        valid_counts.append(count)
                self.min_count = min(valid_counts)

        if new_count < self.min_count and new_count != 0:
            self.min_count = new_count

        if len(self.key_to_count) == 0:
            self.max_count = -1
            self.min_count = -1

    def getMaxKey(self) -> str:
        if self.max_count == -1:
            return ""
        return next(iter(self.count_to_keys[self.max_count]))

    def getMinKey(self) -> str:
        if self.min_count == -1:
            return ""
        return next(iter(self.count_to_keys[self.min_count]))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()