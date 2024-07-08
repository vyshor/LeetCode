class Node:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = Node(val=1)
        ptr = head
        for i in range(2, n+1):
            ptr.next = Node(val=i)
            ptr = ptr.next
        ptr.next = head

        prev, ptr = ptr, head
        count = k-1
        while prev != ptr:
            if count == 0:
                prev.next = ptr.next
                ptr = ptr.next
                count = k-1
            else:
                prev, ptr = ptr, ptr.next
                count -= 1
        return ptr.val
