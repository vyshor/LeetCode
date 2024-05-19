class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # for num in nums:
        #     print("{0:b}".format(num))
        msb = -1
        i = k
        while i:
            msb += 1
            i >>= 1
        msb_count = 0
        maxx_msb = 1 << msb
        mask = (1 << (msb+1))-1
        total = 0
        n = len(nums)
        minn = mask << 1
        mask_total = 0
        # print(msb)
        for num in nums:
            i = num & mask
            total += num ^ i
            if i < maxx_msb:
                i ^= k
            else:
                msb_count += 1
            minn = min(minn, i - (i ^ k))
            mask_total += i
        # print(msb_count)
        non_msb_count = n - msb_count
        # print("Non msb_count:", non_msb_count)
        if non_msb_count % 2 == 1:
            # There must be one that is flipped
            # which you choose the smallest one
            return total + mask_total - minn
        else:
            return mask_total + total
