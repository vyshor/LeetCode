# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        def inOrder(node):
            if node is None:
                return

            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        n = len(arr)
        minn = float('inf')
        for i in range(1, n):
            minn = min(minn, arr[i] - arr[i - 1])
        return minn
