def reverse_bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted in descending order.

    The return value i is such that all e in a[:i] have e >= x, and all e in
    a[i:] have e < x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    Essentially, the function returns number of elements in a which are >= than x.
    >>> a = [8, 6, 5, 4, 2]
    >>> reverse_bisect_right(a, 5)
    3
    >>> a[:reverse_bisect_right(a, 5)]
    [8, 6, 5]
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        for idx, row in enumerate(mat):
            ans.append((reverse_bisect_right(row, 1), idx))
        ans.sort()
        return [x[1] for x in ans[:k]]


# Time: O(nlgm)
# Space: O(n)

# Runtime: 104 ms, faster than 89.22% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.8 MB, less than 16.13% of Python3 online submissions for The K Weakest Rows in a Matrix.