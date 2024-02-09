"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        if node is None:
            return None

        def cloneNode(node):
            clonedNode = Node(val=node.val, neighbors=[])
            visited[node.val] = clonedNode

            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    clonedNode.neighbors.append(cloneNode(neighbor))
                else:
                    clonedNode.neighbors.append(visited[neighbor.val])
            return clonedNode

        return cloneNode(node)
