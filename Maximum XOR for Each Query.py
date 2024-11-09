class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xorr = 0
        maxx = (1 << maximumBit) - 1
        n = len(nums)
        ans = []
        for num in nums:
            xorr ^= num
        for i in range(n-1, -1, -1):
            ans.append((xorr & maxx) ^ maxx)
            xorr ^= nums[i]
        return ans
