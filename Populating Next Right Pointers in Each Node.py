"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        dp = []

        def connectLevel(node, depth):
            if node is None:
                return

            if depth >= len(dp):
                dp.append(node)
            else:
                dp[depth].next = node
                dp[depth] = node

            connectLevel(node.left, depth + 1)
            connectLevel(node.right, depth + 1)

        connectLevel(root, 0)
        return root