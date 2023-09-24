# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node(TreeNode):
    def __init__(self, val=0):
        self.balance = None
        self.height = None
        super().__init__(val=val)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insertNode(val, node):
            if node is None:
                return Node(val=val)
            if val <= node.val:
                node.left = insertNode(val, node.left)
            else:
                node.right = insertNode(val, node.right)

            updateHeight(node)
            updateBalance(node)
            return applyRotation(node)

        def updateHeight(node):
            if node is None:
                return 0

            leftHeight = updateHeight(node.left)
            rightHeight = updateHeight(node.right)
            height = max(leftHeight, rightHeight) + 1
            node.height = height
            return height

        def getHeight(node):
            if node is None:
                return 0

            if node.height is not None:
                return node.height

            return updateHeight(node)

        def updateBalance(node):
            if node is None:
                return 0

            balance = getHeight(node.left) - getHeight(node.right)
            node.balance = balance
            return balance

        def getBalance(node):
            if node is None:
                return 0

            if node.balance is not None:
                return node.balance

            return updateBalance(node)

        def applyRotation(node):
            balance = getBalance(node)
            if balance > 1:
                if getBalance(node.left) < 0:
                    node.left = rotateLeft(node.left)
                return rotateRight(node)
            elif balance < -1:
                if getBalance(node.right) > 0:
                    node.right = rotateRight(node.right)
                return rotateLeft(node)
            else:
                return node

        def rotateRight(node):
            leftNode = node.left
            centreNode = leftNode.right
            leftNode.right = node
            node.left = centreNode

            updateHeight(node)
            updateHeight(leftNode)

            return leftNode

        def rotateLeft(node):
            rightNode = node.right
            centreNode = rightNode.left
            rightNode.left = node
            node.right = centreNode

            updateHeight(node)
            updateHeight(rightNode)

            return rightNode

        root = Node(val=nums[0])
        n = len(nums)
        for i in range(1, n):
            root = insertNode(nums[i], root)
        return root
