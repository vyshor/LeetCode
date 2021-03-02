from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        twice_num = -1
        missing_num = -1
        seen = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in seen:
                missing_num = i
            elif seen[i] == 2:
                twice_num = i
        return [twice_num, missing_num]

# Time: O(n)
# Space: O(n)

# Runtime: 208 ms, faster than 50.33% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.9 MB, less than 55.13% of Python3 online submissions for Set Mismatch.
