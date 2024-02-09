class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start = nums[0]
        prev = nums[0]
        n = len(nums)
        ans = []
        for i in range(1, n):
            if nums[i] != prev + 1:
                if start == prev:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{prev}")
                start = nums[i]

            prev = nums[i]

        if start == prev:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{prev}")

        return ans
    \