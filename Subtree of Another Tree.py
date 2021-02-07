# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkNode(self, n1: TreeNode, n2: TreeNode):
        if type(n1) == type(n2) == type(None):
            return True
        elif type(n1) != type(n2):
            return False
        else:
            return n1.val == n2.val and self.checkNode(n1.left, n2.left) and self.checkNode(n1.right, n2.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.checkNode(t, s) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t) if s and t else False

# Time: O(nm) for n number of nodes in t and m number of nodes in s
# Space: O(1), if don't consider original tree

# Runtime: 604 ms, faster than 5.18% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15 MB, less than 10.00% of Python3 online submissions for Subtree of Another Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if type(s) == type(t) == type(None):
            return True
        elif type(s) == type(None) or type(t) == type(None):
            return False

        def tree2str(tree):
            s_str = ''
            if tree.left:
                tleft = tree.left.val
            else:
                tleft = 'LN'

            if tree.right:
                tright = tree.right.val
            else:
                tright = 'RN'
            s_str += ',#{}'.format(tleft) + (tree2str(tree.left) if tree.left else '') + ',#{}'.format(tright) + (
                tree2str(tree.right) if tree.right else '')
            return s_str

        ss_str = '#{}'.format(s.val) + tree2str(s)
        tt_str = '#{}'.format(t.val) + tree2str(t)
        # print(ss_str)
        # print(tt_str)

        return tt_str in ss_str

# Time: O(n) for n for number of nodes, for string construction | O(n) for string comparison
# Space: O(n) for depth of stack recursion, for a tilted tree

# Runtime: 88 ms, faster than 88.32% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.2 MB, less than 10.00% of Python3 online submissions for Subtree of Another Tree.