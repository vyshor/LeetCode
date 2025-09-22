class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prev = {}
        left_ptr = 0
        right_ptr = 0
        summ = 0
        maxx = 0
        n = len(nums)
        while right_ptr < n:
            num = nums[right_ptr]
            if num in prev:
                for i in range(left_ptr, prev[num]+1):
                    summ -= nums[i]
                left_ptr = max(left_ptr, prev[num]+1)
            summ += num

            maxx = max(maxx, summ)
            prev[num] = right_ptr
            right_ptr += 1
        return maxx
