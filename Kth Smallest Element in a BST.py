# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def findSmallest(node, k):
            if node.left is not None:
                v, k = findSmallest(node.left, k)

                if k == 0:
                    return v, 0

            if k == 1:
                return node.val, 0

            k -= 1

            if node.right is not None:
                v, k = findSmallest(node.right, k)

                if k == 0:
                    return v, 0

            return None, k

        return findSmallest(root, k)[0]



