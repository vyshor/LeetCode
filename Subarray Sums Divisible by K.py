class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        def add(i, j):
            nonlocal k
            i += j
            if i < 0:
                i += k
            return i % k

        n = len(nums)

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

        seen = {0: 1}
        count = 0
        for i in range(1, n+1):
            finding = add(total, -suffixes[i])
            if finding in seen:
                count += seen[finding]
            if prefixes[i-1] not in seen:
                seen[prefixes[i-1]] = 1
            else:
                seen[prefixes[i-1]] += 1
        return count
