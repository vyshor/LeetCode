class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # print(nums)
        # print(prefix)

        ans = []
        for q in queries:
            i = bisect.bisect_left(nums, q)
            if i >= n:
                i = n - 1
            elif nums[i] != q:
                i -= 1
                i = max(i, 0)

            prefix_sum = abs((i + 1) * q - prefix[i])
            suffix_sum = prefix[-1] - prefix[i] - (n - i - 1) * q

            # print(q, i, prefix_sum, suffix_sum, prefix_sum+suffix_sum)
            ans.append(prefix_sum + suffix_sum)

        return ans

