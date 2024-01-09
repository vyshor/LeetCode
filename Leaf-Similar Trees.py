# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1, stack2 = [root1], [root2]

        def getNextLeafNode(stack):
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    return node

                if node.right is not None:
                    stack.append(node.right)

                if node.left is not None:
                    stack.append(node.left)

            return None

        while stack1 and stack2:
            node1, node2 = getNextLeafNode(stack1), getNextLeafNode(stack2)
            if node1.val != node2.val:
                return False

        return len(stack1) == len(stack2)
