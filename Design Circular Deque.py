class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode()
        self.k = k
        self.size = 0
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail

    def insertFront(self, value: int) -> bool:
        if self.size >= self.k:
            return False

        next_node = self.head.next
        node = ListNode(val=value, prev=self.head, next=self.head.next)
        self.head.next = node
        next_node.prev = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        prev_node = self.tail.prev
        node = ListNode(val=value, prev=self.tail.prev, next=self.tail)
        self.tail.prev = node
        prev_node.next = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size < 1:
            return False

        self.head = self.head.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size < 1:
            return False

        self.tail = self.tail.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()