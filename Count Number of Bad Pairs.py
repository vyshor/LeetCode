class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        for i, num in enumerate(nums):
            offset = num - i
            if offset in counter:
                counter[offset] += 1
            else:
                counter[offset] = 1

        count = n * (n - 1) // 2
        for v in counter.values():
            if v > 1:
                count -= v * (v - 1) // 2
        return count


