# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        minn_val = float('-inf')
        count = 0
        maxx = 0
        mode = []

        def exploreNode(node):
            nonlocal count, minn_val, maxx, mode

            if node is None:
                return

            exploreNode(node.left)

            if node.val == minn_val:
                count += 1
            else:
                minn_val = node.val
                count = 1

            if count > maxx:
                maxx = count
                mode = [node.val]
            elif count == maxx:
                mode.append(node.val)

            exploreNode(node.right)

        exploreNode(root)

        return mode

# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         counter = {}
#
#         def exploreNode(node):
#             nonlocal counter
#             if node is None:
#                 return
#
#             if node.val not in counter:
#                 counter[node.val] = 1
#             else:
#                 counter[node.val] += 1
#
#             exploreNode(node.left)
#             exploreNode(node.right)
#
#         exploreNode(root)
#         maxx = max(counter.values())
#         mode = []
#         for v, count in counter.items():
#             if count == maxx:
#                 mode.append(v)
#         return mode
