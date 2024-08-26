"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        arr = [root]
        ans = deque([])
        while arr:
            node = arr.pop()
            ans.appendleft(node.val)
            for child in node.children:
                arr.append(child)
        return ans
