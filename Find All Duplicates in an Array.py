class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = []
        for i in range(n):
            nums[(nums[i]-1)%(n+1)] += (n+1)
        for i in range(n):
            if nums[i] // (n+1) == 2:
                ans.append(i+1)
        return ans
