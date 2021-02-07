# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        node_str = ''

        def serial_node(node):
            nonlocal node_str
            if not node:
                node_str += '_N'
            else:
                node_str += '_{}'.format(node.val)
                serial_node(node.left)
                serial_node(node.right)

        serial_node(root)
        return node_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserial_node(node, node_str):
            if not node:
                return node_str
            str_pt = 1
            ns = ''
            while node_str[str_pt] != '_':
                ns += node_str[str_pt]
                str_pt += 1
            ns2 = node_str[str_pt:]
            if ns == 'N':
                node.left = None
            else:
                node.left = TreeNode(int(ns))
            ns2 = deserial_node(node.left, ns2)

            str_pt = 1
            ns = ''
            while str_pt < len(ns2) and ns2[str_pt] != '_':
                ns += ns2[str_pt]
                str_pt += 1
            ns2 = ns2[str_pt:]

            if ns == 'N':
                node.right = None
            else:
                node.right = TreeNode(int(ns))
            ns2 = deserial_node(node.right, ns2)
            return ns2

        str_pt = 1
        ns = ''
        while data[str_pt] != '_':
            ns += data[str_pt]
            if ns == 'N':
                return None
            str_pt += 1
        ns2 = data[str_pt:]
        root = TreeNode(int(ns))
        deserial_node(root, ns2)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Time: O(n) for unbalanced tree
# Space: O(n) for a chain of BST
# Runtime: 156 ms, faster than 31.28% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 20.4 MB, less than 24.14% of Python3 online submissions for Serialize and Deserialize Binary Tree.