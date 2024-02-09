# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, pt = node, node.next
        while 1:
            prev.val = pt.val

            if pt.next is None:
                prev.next = None
                return

            prev, pt = pt, pt.next