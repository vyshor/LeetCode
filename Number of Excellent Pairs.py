class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        n = len(nums)
        dp = {}
        total_count = 0

        def bit_count(i):
            nonlocal dp
            if i in dp:
                return dp[i]

            count = 0
            while i:
                count += i % 2
                i >>= 1

            dp[i] = count
            return count

        arr = []
        for i in range(n):
            arr.append(bit_count(nums[i]))

        arr.sort()

        # print(arr)

        for i in range(n):
            num = nums[i]
            num_count = bit_count(num)

            if num_count >= k:

                total_count += n
                continue

            j = bisect.bisect_left(arr, k - num_count)
            # print(nums[i], j)
            total_count += n-j

        return total_count
