import operator
class Solution:
    def pop_overlap(self, a, b):
        if b[0] <= a[1] <= b[1] and a[0] <= b[0] <= a[1]:
            a = [a[0], b[1]]
            return a
        elif a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]:
            a = [a[0], a[1]]
            return a
        else:
            return ()

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=operator.itemgetter(1))
        intervals.sort(key=operator.itemgetter(0))
        # Possible because Timesort is stable, rather than using sort by tuple
        # intervals.sort(key=operator.itemgetter(0, 1))
        n = len(intervals)
        r_keys = set(range(n))
        idx = 0
        while idx < n - 1:
            new_a = self.pop_overlap(intervals[idx], intervals[idx + 1])
            if new_a:
                r_keys.remove(idx)
                intervals[idx + 1] = new_a
            idx += 1
        intervals = [intervals[x] for x in r_keys]
        return intervals

# Time: O(nlgn)  [nlgn for timsort, n for checking overlap, n for reconstructing final intervals]
# Space: O(n) [Insert into hash tables remaining intervals to use]
# Runtime: 104 ms, faster than 48.41% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.9 MB, less than 6.52% of Python3 online submissions for Merge Intervals.