class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        i = 0
        for num in nums:
            i ^= num

        bitshift_count = 0
        while i % 2 != 1:
            i = i >> 1
            bitshift_count += 1

        p1, p2 = 0, 0
        for num in nums:
            if (num >> bitshift_count) % 2:
                p1 ^= num
            else:
                p2 ^= num
        return [p1, p2]
