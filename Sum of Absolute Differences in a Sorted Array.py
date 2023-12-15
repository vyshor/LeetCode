class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 0
        prefixes = []
        for num in nums:
            prefix += num
            prefixes.append(prefix)

        arr = []
        for i, num in enumerate(nums):
            arr.append((i + 1) * num - 2 * prefixes[i] + prefixes[-1] - (n - 1 - i) * num)
        return arr
