class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        q = [((), 0)]
        while q:
            comb, i = q.pop()
            if i == n:
                ans.append(comb)
            else:
                q.append((comb, i + 1))
                q.append((comb + (nums[i],), i + 1))
        return ans
