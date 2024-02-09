# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        maxx = 0
        visited = set()
        source = None

        def connectNode(node):
            nonlocal source
            if node is None:
                return

            if node.val == start:
                source = node

            node.parent = None

            if node.left is not None:
                connectNode(node.left)
                node.left.parent = node

            if node.right is not None:
                connectNode(node.right)
                node.right.parent = node

        def infectNode(node, count):
            nonlocal maxx
            if node is None or node in visited:
                return

            count += 1
            maxx = max(count, maxx)
            visited.add(node)

            infectNode(node.parent, count)
            infectNode(node.left, count)
            infectNode(node.right, count)

        connectNode(root)
        infectNode(source, -1)
        return maxx
