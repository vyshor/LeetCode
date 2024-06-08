class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        def add(i, j):
            nonlocal k
            i += j
            if i < 0:
                i += k
            return i % k

        n = len(nums)
        if n == 1:
            return False

        if n == 2:
            return add(nums[0], nums[1]) == 0

        prefixes = [0] * n
        suffixes = [0] * (n+1)
        total = 0
        for i in range(n):
            total = add(total, nums[i])
            prefixes[i] = total

        t = 0
        for i in range(n-1, -1, -1):
            t = add(t, nums[i])
            suffixes[i] = t

        seen = {0}
        for i in range(2, n+1):
            finding = add(total, -suffixes[i])
            if finding in seen:
                return True
            seen.add(prefixes[i-2])
        return False
