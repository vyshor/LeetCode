# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        ans = []

        def isTargetInTree(node):
            nonlocal ans

            if node is None:
                return False, 0

            if node is target:
                findNodeByDist(node, k)
                return True, 1

            inLeftTree, leftDist = isTargetInTree(node.left)
            inRightTree, rightDist = isTargetInTree(node.right)
            dist = 0

            if inLeftTree:
                dist = leftDist
                if leftDist == k:
                    ans.append(node.val)
                elif k > leftDist:
                    findNodeByDist(node.right, k - leftDist - 1)

            if inRightTree:
                dist = rightDist
                if rightDist == k:
                    ans.append(node.val)
                elif k > rightDist:
                    findNodeByDist(node.left, k - rightDist - 1)
            return (inLeftTree or inRightTree), dist + 1

        def findNodeByDist(node, dist):
            nonlocal ans
            if node is None:
                return

            if dist == 0:
                ans.append(node.val)

            findNodeByDist(node.left, dist - 1)
            findNodeByDist(node.right, dist - 1)

        isTargetInTree(root)
        return ans
