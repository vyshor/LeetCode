# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode()], 2: []}
        ans = []

        def duplicateTree(node):
            if node is None:
                return None

            duplicatedNode = TreeNode()
            duplicatedNode.left = duplicateTree(node.left)
            duplicatedNode.right = duplicateTree(node.right)

            return duplicatedNode

        def getBinaryTree(count):
            if count in dp:
                return dp[count]

            trees = []

            for i in range(1, count - 1):
                leftTrees = getBinaryTree(i)
                rightTrees = getBinaryTree(count - i - 1)

                for leftChild in leftTrees:
                    for rightChild in rightTrees:
                        newTree = TreeNode()
                        newTree.left = leftChild
                        newTree.right = rightChild
                        trees.append(newTree)

            dp[count] = trees
            return dp[count]

        getBinaryTree(n)
        return dp[n]
