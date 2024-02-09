class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = {}
        ans = []
        for nums in [nums1, nums2, nums3]:
            for v in set(nums):
                if v not in counter:
                    counter[v] = 1
                else:
                    counter[v] += 1
                    if counter[v] == 2:
                        ans.append(v)
        return ans
