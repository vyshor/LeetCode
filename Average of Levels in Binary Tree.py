# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = {}
        def processNode(node, level):
            if not node:
                return
            if level not in levels:
                levels[level] = (node.val, 1)
            else:
                total, count = levels[level]
                levels[level] = total+node.val, count+1
            processNode(node.left, level+1)
            processNode(node.right, level+1)
        processNode(root, 0)
        ans = []
        for i in range(len(levels)):
            total, count = levels[i]
            ans.append(total/count)
        return ans

# Time: O(n)
# Space: O(n)

# Runtime: 44 ms, faster than 91.77% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 17.5 MB, less than 10.91% of Python3 online submissions for Average of Levels in Binary Tree.
