"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        levels = []

        def addNode(node, depth):
            nonlocal levels
            if depth + 1 > len(levels):
                levels.append([node.val])
            else:
                levels[depth].append(node.val)

            if node.children:
                for child in node.children:
                    addNode(child, depth + 1)

        addNode(root, 0)
        return levels
