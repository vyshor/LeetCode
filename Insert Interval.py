class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        low, high = tuple(newInterval)
        bottom, upper = -1, -1
        bot_val, up_val = low, high
        for idx in range(len(intervals)):
            interval = intervals[idx]
            if low <= interval[1]:
                if bottom == -1:
                    bottom = idx
                    bot_val = min(low, interval[0])
        for idx in range(len(intervals)-1, -1, -1):
            interval = intervals[idx]
            if high >= interval[0]:
                if upper == -1:
                    upper = idx
                    up_val = max(high, interval[1])
        # print(bottom, upper)
        if bottom == -1:
            intervals.insert(len(intervals), newInterval)
            return intervals
        elif upper == -1:
            intervals.insert(0, newInterval)
            return intervals
        if bottom > upper:
            intervals.insert(bottom, newInterval)
            return intervals
        for x in range(bottom, upper):
            intervals.pop(bottom)
        intervals[bottom] = [bot_val, up_val]
        return intervals

# Time: O(n) for first iteration for bottom, another O(n) for upper, O(n) for popping the lists out, total O(n)
# Space: O(1) if you don't consider initial list

# Runtime: 84 ms, faster than 96.07% of Python3 online submissions for Insert Interval.
# Memory Usage: 16.2 MB, less than 8.00% of Python3 online submissions for Insert Interval.