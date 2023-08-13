class Node:
    def __init__(self, key=0, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class LinkedHashMap:
    def __init__(self, newKey):
        self.count = 1
        newNode = Node(key=newKey)
        self.dp = {newKey: newNode}
        self.dummyHead = Node(next=newNode)
        self.dummyTail = Node(prev=newNode)
        newNode.next = self.dummyTail
        newNode.prev = self.dummyHead

    def removeKey(self, key):
        node = self.dp[key]
        node.prev.next, node.next.prev = node.next, node.prev
        del self.dp[key]
        self.count -= 1

    def append(self, key):
        newNode = Node(key=key, next=self.dummyTail)
        self.dp[key] = newNode
        self.dummyTail.prev.next, newNode.prev = newNode, self.dummyTail.prev
        self.dummyTail.prev = newNode
        self.count += 1

    def popleft(self):
        poppedNode = self.dummyHead.next
        poppedNode.next.prev = self.dummyHead
        self.dummyHead.next = poppedNode.next
        self.count -= 1
        del self.dp[poppedNode.key]
        return poppedNode.key


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.dp = {}
        self.use_count = {}
        self.count_to_key = {}
        self.least_use = 0
        self.rolling_key = 0
        self.key_last_use = {}

    def get(self, key: int) -> int:
        if key in self.dp:

            self.key_last_use[key] = self.rolling_key
            self.rolling_key += 1

            prev_count = self.use_count[key]
            new_count = prev_count + 1
            self.use_count[key] = new_count

            self.count_to_key[prev_count].removeKey(key)
            if self.count_to_key[prev_count].count == 0:
                del self.count_to_key[prev_count]

            if new_count not in self.count_to_key:
                self.count_to_key[new_count] = LinkedHashMap(key)
            else:
                self.count_to_key[new_count].append(key)

            if self.least_use == prev_count:
                if prev_count not in self.count_to_key:
                    self.least_use = new_count

            return self.dp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dp:
            if self.current_size >= self.capacity:
                # Eviction
                evicted_key = self.count_to_key[self.least_use].popleft()

                del self.dp[evicted_key]
                del self.key_last_use[evicted_key]
                if self.count_to_key[self.least_use].count == 0:
                    del self.count_to_key[self.least_use]
                if len(self.count_to_key) != 0:
                    self.least_use = min(self.count_to_key.keys())

            # Set of new key
            self.current_size += 1
            self.dp[key] = value
            new_count = 1
            self.use_count[key] = new_count
            self.least_use = new_count

            if new_count not in self.count_to_key:
                self.count_to_key[new_count] = LinkedHashMap(key)
            else:
                self.count_to_key[new_count].append(key)

            self.key_last_use[key] = self.rolling_key
            self.rolling_key += 1
        else:
            # Update key
            self.dp[key] = value
            self.key_last_use[key] = self.rolling_key
            self.rolling_key += 1

            prev_count = self.use_count[key]
            new_count = prev_count + 1
            self.use_count[key] = new_count

            self.count_to_key[prev_count].removeKey(key)
            if self.count_to_key[prev_count].count == 0:
                del self.count_to_key[prev_count]

            if new_count not in self.count_to_key:
                self.count_to_key[new_count] = LinkedHashMap(key)
            else:
                self.count_to_key[new_count].append(key)

            if self.least_use == prev_count:
                if prev_count not in self.count_to_key:
                    self.least_use = new_count

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
