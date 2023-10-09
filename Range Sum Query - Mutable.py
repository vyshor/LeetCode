class Node:
    def __init__(self, val=0, left=None, right=None, low=0, high=0):
        self.val = val
        self.left = left
        self.right = right
        self.low = low
        self.high = high


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.root = self.addNode(0, self.n - 1)

    def addNode(self, lo, hi):
        if lo == hi:
            return Node(val=self.nums[lo], low=lo, high=hi)

        mid = (lo + hi) // 2
        node = Node(low=lo, high=hi)
        node.left = self.addNode(lo, mid)
        node.right = self.addNode(mid + 1, hi)
        node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
        return node

    def update(self, index: int, val: int) -> None:
        net_change = val - self.nums[index]
        self.nums[index] = val

        self.updateNode(self.root, index, net_change)

    def updateNode(self, node, i, change):
        if node is None:
            return

        if node.low <= i <= node.high:
            node.val += change
            self.updateNode(node.left, i, change)
            self.updateNode(node.right, i, change)

    def sumNode(self, node, lo, hi):
        if hi < node.low or lo > node.high:
            return 0

        if node.low == lo and node.high == hi:
            return node.val

        mid = (node.low + node.high) // 2
        return self.sumNode(node.left, lo, min(hi, mid)) + self.sumNode(node.right, max(lo, mid + 1), hi)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumNode(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
