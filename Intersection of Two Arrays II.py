class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        ans = []
        for num in nums2:
            if counter[num] > 0:
                ans.append(num)
                counter[num] -= 1
        return ans

