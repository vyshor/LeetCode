class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums:
            return True

        # Backward
        backward = True
        prev = nums[-1]
        modifyOne = False
        for num in nums[::-1]:
            if num > prev:
                if not modifyOne:
                    modifyOne = True
                else:
                    backward = False
                    break
            else:
                prev = num

        # Forward
        forward = True
        prev = nums[0]
        modifyOne = False
        for num in nums:
            if num < prev:
                if not modifyOne:
                    modifyOne = True
                else:
                    forward = False
                    break
            else:
                prev = num
        return backward or forward

# Time: O(n)
# Space: O(1)

# Runtime: 184 ms, faster than 58.12% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.4 MB, less than 63.92% of Python3 online submissions for Non-decreasing Array.

