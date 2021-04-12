# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level_sum = [0]
        def exploreNode(node, depth):
            if not node:
                return
            if depth >= len(level_sum):
                level_sum.append(0)
            level_sum[depth] += node.val
            exploreNode(node.left, depth+1)
            exploreNode(node.right, depth+1)
        exploreNode(root, 0)
        return level_sum[-1]

# Time: O(N)
# Space: O(N)

# Runtime: 88 ms, faster than 86.16% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.9 MB, less than 40.84% of Python3 online submissions for Deepest Leaves Sum.
