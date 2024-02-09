class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        diffs = [0] * n

        for i in range(n):
            diffs[i] = nums1[i] - nums2[i]

        prev = [diffs[0]]
        count = 0
        for i in range(1, n):
            remaining = diff + diffs[i]
            j = bisect.bisect_right(prev, remaining)

            count += j
            bisect.insort_left(prev, diffs[i])

        return count

# nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
# nums1[i] - nums2[i] + (nums2[j] - nums1[j]) <= diff
# d(i) + (-d(j)) <= diff
# d(i)-d(j) <= diff
# d(i) <= diff+d(j)
