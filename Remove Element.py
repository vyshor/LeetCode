class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        count = 0
        start, end = 0, n-1
        while start <= end:
            if nums[start] == val:
                while nums[end] == val:
                    end -= 1
                    if end <= start:
                        return count
                else:
                    nums[start], nums[end] = nums[end], nums[start]
                    count += 1
                    start += 1
                    end -= 1
            else:
                count += 1
                start += 1
        return count
