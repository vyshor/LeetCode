class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(num, i) for i, num in enumerate(nums)]
        q.sort()

        valid_i = set()
        ans = []
        for i in range(n - k, n):
            valid_i.add(q[i][1])

        for i in range(n):
            if i in valid_i:
                ans.append(nums[i])

        return ans
