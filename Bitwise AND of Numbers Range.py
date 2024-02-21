class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        original = right

        total_bits, similar_bits = 0, 0
        while left > 0 and right > 0:
            if left & 1 == right & 1:
                similar_bits += 1
            else:
                similar_bits = 0

            total_bits += 1
            left >>= 1
            right >>= 1

        # print(total_bits, similar_bits)
        if left == 0 and right == 0:
            original >>= total_bits - similar_bits
            original <<= total_bits - similar_bits
            return original
        else:
            return 0

# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         lower, upper = left, right
#         count = 0
#         while lower != upper:
#             lower >>= 1
#             upper >>= 1
#             count += 1
#
#         return lower << count
#
# # 2: 0010
# # 4: 0100
#
# # 5: 0101
# # 6: 0110
# # 7: 0111
# # 8: 1000
