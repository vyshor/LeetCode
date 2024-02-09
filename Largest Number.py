class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def numCompare(s1, s2):
            if s1+s2 > s2+s1:
                return -1
            elif s1+s2 < s2+s1:
                return 1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(numCompare))
        # print(nums)
        return str(int(''.join(nums)))
