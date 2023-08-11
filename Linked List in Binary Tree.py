# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def seekNode(node):
            if seekPath(node, head):
                return True

            if node.left and seekNode(node.left):
                return True
            if node.right and seekNode(node.right):
                return True

        def seekPath(node, pt):
            if pt is None:
                return True

            if node.val == pt.val:
                pt = pt.next
                if pt is None:
                    return True

                if node.left and seekPath(node.left, pt):
                    return True
                if node.right and seekPath(node.right, pt):
                    return True
            return False

        return seekNode(root)
