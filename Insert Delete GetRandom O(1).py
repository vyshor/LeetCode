class RandomizedSet:

    def __init__(self):
        self.dp = {}
        self.order = []

    def insert(self, val: int) -> bool:
        exists = val in self.dp
        if not exists:
            self.dp[val] = len(self.order)
            self.order.append(val)
        return not exists

    def remove(self, val: int) -> bool:
        exists = val in self.dp
        if exists:
            last, i = len(self.order) - 1, self.dp[val]
            self.order[last], self.order[i] = self.order[i], self.order[last]
            self.dp[self.order[i]] = i
            del self.dp[val]
            self.order.pop()
        return exists

    def getRandom(self) -> int:
        return self.order[random.randint(0, len(self.order) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# import random
#
#
# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = {}
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if self.d.get(val):
#             return False
#         else:
#             self.d[val] = True
#             return True
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if self.d.get(val):
#             del self.d[val]
#             return True
#         else:
#             return False
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         return random.choice(list(self.d.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Time Complexity: O(1)
# Space Complexity: O(n) for n maximum number of elements at any given point

# Runtime: 396 ms, faster than 33.29% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 17.9 MB, less than 54.54% of Python3 online submissions for Insert Delete GetRandom O(1).