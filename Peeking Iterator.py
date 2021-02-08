# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        ans, self.buffer = self.buffer, self.iterator.next() if self.iterator.hasNext() else None
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

# Runtime: 28 ms, faster than 88.74% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.5 MB, less than 66.46% of Python3 online submissions for Peeking Iterator.

# Time: O(1)
# Space: O(1)