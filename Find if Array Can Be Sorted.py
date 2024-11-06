class Solution:
    def countBits(self, num):
        count = 0
        while num:
            count += num % 2
            num >>= 1
        return count

    def canSortArray(self, nums: List[int]) -> bool:
        i = 1
        prev_maxx = 0
        minn = nums[0]
        maxx = nums[0]
        bit_count = self.countBits(nums[0])
        n = len(nums)
        while i < n:
            num = nums[i]
            bcount = self.countBits(num)
            if bcount != bit_count:
                # Check if current period is sortable to previous period
                if minn < prev_maxx:
                    return False
                prev_maxx = maxx
                minn = num
                maxx = num
                bit_count = bcount
            else:
                minn = min(minn, num)
                maxx = max(maxx, num)
            i += 1

        return not minn < prev_maxx

# class Solution:
#     def canSortArray(self, nums: List[int]) -> bool:
#         def countBits(num):
#             count = 0
#             while num > 0:
#                 count += num % 2
#                 num >>= 1
#             return count
#
#         n = len(nums)
#         prev_bits = countBits(nums[0])
#         maxx = 0
#         prev = nums[0]
#         for i in range(1, n):
#             bits = countBits(nums[i])
#             # print(nums[i], bits, prev_bits, maxx, prev)
#             if bits == prev_bits:
#                 if nums[i] < maxx:
#                     return False
#                 prev = max(prev, nums[i])
#                 continue
#             elif nums[i] < prev:
#                 return False
#
#             maxx, prev = prev, max(prev, nums[i])
#             prev_bits = bits
#         return True
