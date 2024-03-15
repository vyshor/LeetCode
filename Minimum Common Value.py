class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while nums1[p1] != nums2[p2]:
            while p1 < n1 and nums1[p1] < nums2[p2]:
                p1 += 1

            if p1 == n1:
                return -1

            while p2 < n2 and nums2[p2] < nums1[p1]:
                p2 += 1

            if p2 == n2:
                return -1

        if nums1[p1] == nums2[p2]:
            return nums1[p1]

        return -1
