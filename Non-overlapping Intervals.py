class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        # intervals.sort(key=lambda x: x[0])
        max_val = intervals[0][1]
        min_num = 0
        for interval in intervals[1:]:
            if interval[0] < max_val:
                min_num += 1
            else:
                max_val = interval[1]
        return min_num

# Time: O(nlgn)
# Space: O(1)
# Runtime: 84 ms, faster than 67.16% of Python3 online submissions for Non-overlapping Intervals.
# Memory Usage: 17.2 MB, less than 25.00% of Python3 online submissions for Non-overlapping Intervals.