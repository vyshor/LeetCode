class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countBits(num):
            count = 0
            while num > 0:
                count += num % 2
                num >>= 1
            return count

        n = len(nums)
        prev_bits = countBits(nums[0])
        maxx = 0
        prev = nums[0]
        for i in range(1, n):
            bits = countBits(nums[i])
            # print(nums[i], bits, prev_bits, maxx, prev)
            if bits == prev_bits:
                if nums[i] < maxx:
                    return False
                prev = max(prev, nums[i])
                continue
            elif nums[i] < prev:
                return False

            maxx, prev = prev, max(prev, nums[i])
            prev_bits = bits
        return True
