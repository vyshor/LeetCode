# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        trees = []

        def recur(node):
            if node is None:
                return

            recur(node.left)
            trees.append(node)
            recur(node.right)

        recur(root)
        n = len(trees)
        if n == 2:
            trees[0].val, trees[1].val = trees[1].val, trees[0].val
            return

        wrongA, wrongB = None, None
        for i in range(1, n):
            if trees[i - 1].val > trees[i].val:
                wrongA = trees[i]
        for i in range(n - 2, -1, -1):
            if trees[i].val > trees[i + 1].val:
                wrongB = trees[i]
        wrongA.val, wrongB.val = wrongB.val, wrongA.val

