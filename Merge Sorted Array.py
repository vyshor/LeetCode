class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = -1
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return
        n -= 1
        m -= 1
        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i]= nums1[m]
                m -= 1
            i -= 1
        if m < 0:
            nums1[:i+1] = nums2[:n+1]

# Runtime: 40 ms, faster than 34.70% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.3 MB, less than 29.25% of Python3 online submissions for Merge Sorted Array.

# Time: O(n+m)
# Space: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1, n2 = 0, 0
        q = []
        if n == 0:
            return
        while n1 < m and n2 < n:
            if nums2[n2] < nums1[n1]:
                q.append(nums2[n2])
                n2 += 1
            else:
                q.append(nums1[n1])
                n1 += 1
        if n1 >= m:
            nums1[:] = q + nums2[n2:]
        else:
            nums1[:] = q + nums1[n1:m]

# Runtime: 60 ms, faster than 5.57% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.4 MB, less than 29.25% of Python3 online submissions for Merge Sorted Array.

# Time: O(n+m)
# Space: O(n+m)