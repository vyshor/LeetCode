class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dp = {}
        nums.sort()

        def recur(leftover):
            if len(leftover) == 1:
                return [leftover]

            combins = []
            if str(leftover) in dp:
                combins = dp[str(leftover)]
            else:
                for i, num in enumerate(leftover):
                    for arr in recur(leftover[:i] + leftover[i + 1:]):
                        combins.append([num] + arr)
                dp[str(leftover)] = combins

            return combins

        return recur(nums)

