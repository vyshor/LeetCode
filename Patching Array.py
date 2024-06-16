class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        total = 0
        m = len(nums)
        ans = 0
        j = 1
        while j <= n:
            while i < m and nums[i] <= j:
                total += nums[i]
                i += 1

            # print(total, j)
            if total < j:
                ans += 1
                total += j
            j = total+1

        return ans
