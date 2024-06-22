class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix = []
        subfix = []
        for i, num in enumerate(nums):
            if num % 2:
                prefix.append(count)
                count = 1
            else:
                count += 1

        if count:
            prefix.append(count)

        count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] % 2:
                subfix.append(count)
                count = 1
            else:
                count += 1

        if count:
            subfix.append(count)

        # print(prefix)
        # print(subfix)

        i = k
        j = len(subfix) - 1
        summ = 0
        while i < len(prefix):
            summ += prefix[i] * subfix[j]
            # print(i, j, summ)
            i += 1
            j -= 1

        return summ
