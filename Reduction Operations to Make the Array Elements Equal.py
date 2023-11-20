class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        counter = Counter(nums)
        count = 0
        n = len(arr)
        for i in range(1, n):
            num = arr[i]
            count += counter[num] * i
        return count
