class Node:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.n = 997
        self.arr = [None] * self.n

    def put(self, key: int, value: int) -> None:
        slot = key % self.n

        dummyHead = Node(next=self.arr[slot])
        prev, pt = dummyHead, dummyHead.next
        updatedVal = False

        while pt is not None:
            if pt.key == key:
                pt.val = value
                updatedVal = True
                break
            else:
                prev, pt = pt, pt.next

        if not updatedVal:
            prev.next = Node(key=key, val=value)

        self.arr[slot] = dummyHead.next

    def get(self, key: int) -> int:
        slot = key % self.n

        pt = self.arr[slot]
        while pt is not None:
            if pt.key == key:
                return pt.val
            else:
                pt = pt.next
        return -1

    def remove(self, key: int) -> None:
        slot = key % self.n

        dummyHead = Node(next=self.arr[slot])
        prev, pt = dummyHead, dummyHead.next

        while pt is not None:
            if pt.key == key:
                prev.next = pt.next
                break
            else:
                prev, pt = pt, pt.next

        self.arr[slot] = dummyHead.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# class MyHashMap:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.table = [None] * 1000001
#
#
#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         self.table[key] = value
#
#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         val = self.table[key]
#         if val is not None:
#             return val
#         else:
#             return -1
#
#
#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         self.table[key] = None



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Time:
#   Put: O(1)
#   Get: O(1)
#   Remove: O(1)
# Space: O(1)

# Runtime: 376 ms, faster than 26.34% of Python3 online submissions for Design HashMap.
# Memory Usage: 39.5 MB, less than 10.82% of Python3 online submissions for Design HashMap.


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = dict()


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.table[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.table:
            return self.table[key]
        else:
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.table:
            del self.table[key]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Time:
#   Put: O(1)
#   Get: O(1)
#   Remove: O(1)
# Space: O(n)

# Runtime: 164 ms, faster than 99.75% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.2 MB, less than 80.28% of Python3 online submissions for Design HashMap.
