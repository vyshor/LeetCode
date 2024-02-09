class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        last_idx = {}
        max_diff = {}

        for i, num in enumerate(nums):
            last_idx[num] = i

        for i, num in enumerate(nums):
            if i == last_idx[num]:
                max_diff[num] = n
                continue

            dist = i - last_idx[num]
            if last_idx[num] > i:
                dist = n - (last_idx[num] - i)

            last_idx[num] = i

            if num not in max_diff:
                max_diff[num] = dist
            else:
                max_diff[num] = max(max_diff[num], dist)

        double_min_seconds = min(max_diff.values())
        return double_min_seconds // 2
