class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False

        intervals = []

        lo = nums[0]
        for i in range(1, n):
            # print(intervals, nums[i])

            # Check if num is in any existing
            if intervals:
                j = bisect.bisect_left(intervals, (nums[i],))
                if j < len(intervals):
                    if j - 1 >= 0 and intervals[j - 1][0] < nums[i] < intervals[j - 1][1]:
                        return True
                else:
                    lower, upper = intervals[-1]
                    if lower < nums[i] < upper:
                        return True

            # Add in new range
            if nums[i] > lo:
                hi = nums[i]
                j = bisect.bisect_left(intervals, (lo, hi))
                if j < len(intervals):
                    if j - 1 >= 0 and (lo < intervals[j - 1][1] or intervals[j - 1][0] < hi):
                        low, high = intervals[j - 1]
                        intervals[j - 1] = min(low, lo), max(high, hi)
                        k = j - 1
                    else:
                        intervals.insert(j, (lo, hi))
                        k = j

                    # Merge interval
                    if k + 1 < len(intervals) and intervals[k][1] > intervals[k + 1][0]:
                        intervals[k] = min(intervals[k][0], intervals[k + 1][0]), max(intervals[k][1],
                                                                                      intervals[k + 1][1])
                        intervals.pop(k + 1)

                else:
                    intervals.append((lo, hi))
            else:
                lo = min(lo, nums[i])

        return False
