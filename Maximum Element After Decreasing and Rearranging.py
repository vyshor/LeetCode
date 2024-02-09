class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        counter = Counter(arr)
        nums = sorted(set(arr))
        count = 0
        for num in nums:
            count += counter[num]
            count = min(count, num)

        return count
