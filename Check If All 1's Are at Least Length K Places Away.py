class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            idx = nums.index(1)
        except:
            return True
        count = 0
        for i in range(idx+1, len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                else:
                    count = 0
            else:
                count += 1
        return True

# Runtime: 540 ms, faster than 94.41% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
# Memory Usage: 17.1 MB, less than 26.17% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.

# Time: O(n)
# Space: O(1)