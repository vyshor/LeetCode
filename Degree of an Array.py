class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        counter = {}
        degree = 0
        ans = len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

            if counter[num] > degree:
                degree = counter[num]
                ans = i - first[num] + 1
            elif counter[num] == degree:
                ans = min(ans, i - first[num] + 1)

        return ans
