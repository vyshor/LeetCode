class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        a1, a2 = 0, 0
        for num, count in counter1.items():
            if num in counter2:
                a1 += count

        for num, count in counter2.items():
            if num in counter1:
                a2 += count
        return [a1, a2]

