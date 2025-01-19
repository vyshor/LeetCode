class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0
        if n2 % 2 == 1:
            for num in nums1:
                ans ^= num
        if n1 % 2 == 1:
            for num in nums2:
                ans ^= num
        return ans
