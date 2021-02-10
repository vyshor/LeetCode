"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_ref = {}
        node = head
        dummy_head = Node(-1)
        prev_node = dummy_head
        while node != None:
            new_node = Node(node.val)
            prev_node.next = new_node
            node_ref[id(node)] = (new_node, id(node.random) if node.random else None)
            prev_node = prev_node.next
            node = node.next

        for old_node_id, (new_node, random_node_id) in node_ref.items():
            if random_node_id:
                new_node.random = node_ref[random_node_id][0]
        return dummy_head.next

# Time: O(n)
# Space: O(n)

# Runtime: 36 ms, faster than 68.57% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.2 MB, less than 29.95% of Python3 online submissions for Copy List with Random Pointer.