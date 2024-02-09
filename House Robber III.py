# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robNode(node):
            # Leaf node
            if node.left is None and node.right is None:
                # print(node.val, 0)
                return node.val, 0

            else:
                robLeft, notRobLeft = 0, 0
                if node.left is not None:
                    robLeft, notRobLeft = robNode(node.left)

                robRight, notRobRight = 0, 0
                if node.right is not None:
                    robRight, notRobRight = robNode(node.right)

                # print(node.val+notRobRight+notRobLeft, robLeft+robRight)
                return node.val + notRobRight + notRobLeft, max(robLeft + robRight, notRobRight + notRobLeft,
                                                                notRobLeft + robRight, robLeft + notRobRight)

        return max(robNode(root))
