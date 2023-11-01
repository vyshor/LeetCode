# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}

        def exploreNode(node):
            nonlocal counter
            if node is None:
                return

            if node.val not in counter:
                counter[node.val] = 1
            else:
                counter[node.val] += 1

            exploreNode(node.left)
            exploreNode(node.right)

        exploreNode(root)
        maxx = max(counter.values())
        mode = []
        for v, count in counter.items():
            if count == maxx:
                mode.append(v)
        return mode
