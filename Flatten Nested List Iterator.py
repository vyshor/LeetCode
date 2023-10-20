# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque(nestedList)
        while self.q and not self.q[0].isInteger():
            v = self.q.popleft()
            _list = v.getList()
            n = len(_list)
            for i in range(n - 1, -1, -1):
                self.q.appendleft(_list[i])

    def next(self) -> int:
        v = self.q.popleft()
        while self.q and not self.q[0].isInteger():
            v2 = self.q.popleft()
            _list = v2.getList()
            n = len(_list)
            for i in range(n - 1, -1, -1):
                self.q.appendleft(_list[i])
        return v.getInteger()

    def hasNext(self) -> bool:
        return bool(self.q)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.dp = self.unravel(nestedList)
#         self.pt = 0
#
#     def unravel(self, nestedList):
#         flatten = []
#         for nested in nestedList:
#             if nested.isInteger():
#                 flatten.append(nested.getInteger())
#             else:
#                 flatten += self.unravel(nested.getList())
#         return flatten
#
#     def next(self) -> int:
#         num = self.dp[self.pt]
#         self.pt += 1
#         return num
#
#     def hasNext(self) -> bool:
#         return self.pt < len(self.dp)

