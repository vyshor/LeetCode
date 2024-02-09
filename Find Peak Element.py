class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        start, end = 0, n - 1

        while start < end:
            if end - start + 1 < 3:
                maxx = nums[start]
                maxx_idx = start
                i = start + 1
                while i <= end:
                    if nums[i] > maxx:
                        maxx_idx = i
                        maxx = nums[i]
                    i += 1
                return maxx_idx

            mid = (start + end) // 2
            prev = mid - 1
            next = mid + 1
            if nums[prev] < nums[mid] > nums[next]:
                return mid
            elif nums[prev] < nums[mid] < nums[next]:
                start = next
            else:
                end = prev

        return start
