class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        summ = 0
        for i in range(n):
            summ += nums[i]
            prefix[i + 1] = summ

        total = summ
        summ = 0
        for i in range(n - 1, -1, -1):
            summ += nums[i]
            suffix[i] = summ

        # print(prefix)
        # print(suffix)
        arr = []
        for i in range(n):
            for j in range(i, n):
                arr.append((total - prefix[i] - suffix[j + 1]) % MOD)

        arr.sort()
        # print(arr)
        summ = 0
        for i in range(left - 1, right):
            summ += arr[i]
            summ %= MOD
        return summ
