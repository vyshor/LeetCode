# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validBST(root, val, lr):
            if not root:
                return True
            elif (root.val >= val if lr == 0 else False) or (root.val <= val if lr == 1 else False) :
                return False
            else:
                return validBST(root.left, root.val,0) and validBST(root.right, root.val, 1) and (validBST(root.left, val, 1) if lr == 1 else True) and (validBST(root.right, val, 0) if lr == 0 else True)
            #and (root.left.val < root.val if root.left else True) and (root.right.val > root.val if root.right else True)
        return validBST(root, root.val, 2) if root else True

# Exceed time limit
# Time complexity is exponential

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            ans = (self.isValidBST(root.left) if root.left else True) and (
                self.isValidBST(root.right) if root.right else True)
            lmax = root.left.max if root.left and hasattr(root.left, 'max') else root.val - 1
            if root.val <= lmax:
                return False

            rmin = root.right.min if root.right and hasattr(root.right, 'min') else root.val + 1
            if root.val >= rmin:
                return False

            lmin = root.left.min if root.left and hasattr(root.left, 'min') else root.val
            rmax = root.right.max if root.right and hasattr(root.right, 'max') else root.val
            root.max = max(root.val, rmax)
            root.min = min(root.val, lmin)
            return ans

# Time: O(n)
# Space: O(n) # Recursive with DP
# Runtime: 64 ms, faster than 11.68% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.8 MB, less than 5.75% of Python3 online submissions for Validate Binary Search Tree.