class Node:
    def __init__(self, key="", next=None):
        self.key = key
        self.next = next


class MyHashSet:

    def __init__(self):
        self.n = 100001
        self.arr = [None] * self.n

    def add(self, key: int) -> None:
        idx = key % self.n
        dummyHead = Node(next=self.arr[idx])
        prev, pt = dummyHead, dummyHead.next
        found = False
        while pt is not None:
            if pt.key == key:
                return

            prev, pt = pt, pt.next

        prev.next = Node(key=key)
        self.arr[idx] = dummyHead.next

    def remove(self, key: int) -> None:
        idx = key % self.n
        dummyHead = Node(next=self.arr[idx])
        prev, pt = dummyHead, dummyHead.next
        while pt is not None:
            if pt.key == key:
                prev.next = pt.next
                break

            prev, pt = pt, pt.next
        self.arr[idx] = dummyHead.next

    def contains(self, key: int) -> bool:
        idx = key % self.n
        pt = self.arr[idx]
        while pt is not None:
            if pt.key == key:
                return True

            pt = pt.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
