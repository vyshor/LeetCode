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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes = []
        node = head
        while node is not None:
            nodes.append(node.val)
            node = node.next
        def buildTree(low, high):
            if low > high:
                return None
            if low == high:
                return TreeNode(val=nodes[low])
            else:
                mid = (high+low)//2
                subroot = TreeNode(val=nodes[mid])
                subroot.left = buildTree(low, mid-1)
                subroot.right = buildTree(mid+1, high)
                return subroot
        return buildTree(0, len(nodes)-1)

# Time: O(n)
# Space: O(n)

# Runtime: 116 ms, faster than 98.45% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.5 MB, less than 15.16% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
