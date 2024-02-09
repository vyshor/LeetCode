class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = []
        for num in arr:
            i = num
            count = 0
            while i > 0:
                count += i % 2
                i >>= 1
            nums.append((count, num))

        nums.sort()
        return [num[1] for num in nums]
