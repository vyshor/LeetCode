class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k
        self.size = 0
        self.front = 0
        self.end = 0


    def enQueue(self, value: int) -> bool:
        if self.size < self.k:
            self.q[self.end%self.k] = value
            self.end += 1
            self.size += 1
            return True
        else:
            return False


    def deQueue(self) -> bool:
        if self.size:
            self.front += 1
            self.size -= 1
            return True
        else:
            return False


    def Front(self) -> int:
        if self.size:
            return self.q[self.front%self.k]
        else:
            return -1


    def Rear(self) -> int:
        if self.size:
            return self.q[(self.end-1)%self.k]
        else:
            return -1


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k

# Time:
#     Init:O(k)
#     Enqueue: O(1)
#     Dequeue: O(1)
#     Front: O(1)
#     End: O(1)
#     IsEmpty: O(1)
#     IsFull: O(1)
# Space: O(k)

# Runtime: 68 ms, faster than 72.79% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 14.5 MB, less than 93.16% of Python3 online submissions for Design Circular Queue.


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()