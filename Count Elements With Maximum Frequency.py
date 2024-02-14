class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        max_count = 0
        maxx = 0
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

            if counter[num] > maxx:
                maxx = counter[num]
                max_count = 1
            elif counter[num] == maxx:
                max_count += 1
        return max_count * maxx
