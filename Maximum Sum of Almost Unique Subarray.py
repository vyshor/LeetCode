class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        counter = Counter(nums[:k])
        maxx = 0
        summ = sum(nums[:k])

        if len(counter) >= m:
            maxx = max(maxx, summ)

        for i in range(k, n):
            summ += nums[i] - nums[i - k]

            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1

            counter[nums[i - k]] -= 1
            if counter[nums[i - k]] == 0:
                del counter[nums[i - k]]

            if len(counter) >= m:
                maxx = max(maxx, summ)

        return maxx
