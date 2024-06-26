# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def read(node):
            nonlocal arr
            if node is None:
                return

            read(node.left)
            arr.append(node.val)
            read(node.right)

        read(root)

        def balance(left, right):
            nonlocal arr
            if left == right:
                return TreeNode(val=arr[left])

            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(val=arr[mid])
            node.left = balance(left, mid - 1)
            node.right = balance(mid + 1, right)
            return node

        return balance(0, len(arr) - 1)

