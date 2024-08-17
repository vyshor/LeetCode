class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxx = max(nums)
        prefixes = []
        count = 0
        total = 0
        for i in range(n):
            if nums[i] == maxx:
                prefixes.append(count + 1)
                count = 0
                total += 1
            else:
                count += 1

        if total < k:
            return 0

        suffixes = []
        count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == maxx:
                suffixes.append(n - i)

        # print(prefixes)
        # print(suffixes)
        summ = 0
        for i in range(total - k + 1):
            # print(i, total - k - i)
            summ += prefixes[i] * suffixes[total - k - i]
        return summ

