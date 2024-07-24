class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(i):
            if i == 0:
                return mapping[i]

            j = 0
            m = 0
            while i:
                j += mapping[(i % 10)] * (10 ** m)
                m += 1
                i //= 10
            return j

        nums = sorted([(convert(num), i, num) for i, num in enumerate(nums)])
        # print(nums)
        nums = [num for (_, _, num) in nums]
        return nums
