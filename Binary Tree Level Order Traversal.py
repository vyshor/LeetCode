# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def saveLevel(node, depth):
            if not node:
                return
            if len(ans) < depth + 1:
                ans.append([node.val])
            else:
                ans[depth].append(node.val)
            saveLevel(node.left, depth+1)
            saveLevel(node.right, depth+1)
        saveLevel(root, 0)
        return ans

# Time: O(n)
# Space: O(n) for one sided BST
# Runtime: 40 ms, faster than 80.33% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.5 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.