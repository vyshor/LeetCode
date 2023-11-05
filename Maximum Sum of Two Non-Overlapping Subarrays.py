class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        summ1, summ2 = [], []
        summ = 0
        for i in range(firstLen - 1):
            summ += nums[i]

        for i in range(firstLen - 1, n):
            summ += nums[i]
            summ1.append(summ)
            summ -= nums[i - (firstLen - 1)]

        summ = 0
        for i in range(secondLen - 1):
            summ += nums[i]

        for i in range(secondLen - 1, n):
            summ += nums[i]
            summ2.append(summ)
            summ -= nums[i - (secondLen - 1)]

        maxx = 0
        # print(summ1)
        # print(summ2)
        n1, n2 = len(summ1), len(summ2)
        for i in range(n1):
            for j in range(n2):
                if i == j:
                    continue

                if i < j and i + firstLen - 1 >= j:
                    continue

                if j < i and j + secondLen - 1 >= i:
                    continue

                maxx = max(maxx, summ1[i] + summ2[j])
        return maxx
