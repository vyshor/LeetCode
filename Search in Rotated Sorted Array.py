class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

# Time: O(n)
# Space: O(1)
# Runtime: 44 ms, faster than 94.39% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
# Wrong method, but it seems like it is faster, perhaps because the n for test cases is significantly small



# 0
# 0

# 0 1
# 0

# 0 1 2 3
#   1

# 0 1 2 3 4
#     2

# 5 1 3
#   1
# Pivot left side
# target not on right side
# 5

# Check mid
# If mid is not, try to locate where the number might be
# Need to check if pivot point is in this arraay
# If there is pivot
# Need to be aware if the left and right contains the pivot point or not
# If left contains pivot, nums[start] > nums[mid]
# Target need to be smaller than mid, and larger than start
# Then iterate through left
# Otherwise iterate through right (target bigger than mid, but smaller than start)
# Else if no pivot

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        if end == -1:
            return -1
        while True:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            try:
                if start == end:
                   return -1
                elif nums[start] > nums[end]: # Check if pivot in array
                    if nums[start] > nums[mid]: # Check if pivot is on the left side
                        if nums[mid] < target <= nums[end]: # Check if target on right side
                            start = mid + 1
                        elif mid > start:
                            end = mid - 1
                        else:
                            return -1
                    else: # Pivot is on right side
                        if nums[start] <= target < nums[mid]: # Check if target on left side
                            if mid > start:
                                end = mid - 1
                            else:
                                return -1
                        else:
                            start = mid + 1
                else:
                    if nums[mid] < target:
                        start = mid+1
                    elif mid > start:
                        end = mid-1
                    else:
                        return -1
            except IndexError:
                return -1

# Time: O(lgn)
# Space: O(1)
# Runtime: 48 ms, faster than 77.96% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.