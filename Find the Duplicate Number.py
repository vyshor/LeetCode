class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slower = nums[0]
        while slower != slow:
            slow = nums[slow]
            slower = nums[slower]

        return slower