class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        xor2 = xor
        first_diff = 0
        while xor2 % 2 == 0:
            first_diff += 1
            xor2 >>= 1

        xor2 = 0
        for num in nums:
            if (1 << first_diff) & num:
                xor2 ^= num
        xor ^= xor2
        return [xor, xor2]

# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         i = 0
#         for num in nums:
#             i ^= num
#
#         bitshift_count = 0
#         while i % 2 != 1:
#             i = i >> 1
#             bitshift_count += 1
#
#         p1, p2 = 0, 0
#         for num in nums:
#             if (num >> bitshift_count) % 2:
#                 p1 ^= num
#             else:
#                 p2 ^= num
#         return [p1, p2]
