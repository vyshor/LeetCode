class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        nums = set(arr)
        dp = {}

        def getTrees(num):
            if num in dp:
                return dp[num]

            # print(num)
            count = 1
            j = 0
            limit = int(math.sqrt(num)) + 1

            while arr[j] < limit:
                other_factor = num // arr[j]
                if num % arr[j] == 0 and other_factor in nums:
                    if arr[j] == other_factor:
                        count += getTrees(arr[j]) * getTrees(other_factor)
                    else:
                        count += 2 * getTrees(arr[j]) * getTrees(other_factor)

                limit = other_factor
                j += 1

            dp[num] = count % MOD
            return dp[num]

        total_count = 0
        for num in arr:
            total_count += getTrees(num)

        # print(dp)

        return total_count % MOD
