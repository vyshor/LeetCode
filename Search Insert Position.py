class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def findTarget(start, end, target):
            if start >= end:
                if target > nums[start]:
                    return start + 1
                return start

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return findTarget(start, mid - 1, target)
            else:
                return findTarget(mid + 1, end, target)

        return findTarget(0, len(nums) - 1, target)
