class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        dp = {'1': nums[0], '0': 0}

        for idx, num in enumerate(nums[1:]):
            idx += 1

            for k in list(dp.keys()):
                if k[-1] == '0':
                    # Choose to rob
                    if idx != len(nums) - 1 or k[0] != '1':
                        dp[k + '1'] = dp[k] + num

                # Choose not to rob
                dp[k + '0'] = dp[k]

            # Only keep the most optimal results
            dpa = {}
            for first_record in ['0', '1']:
                for last_record in ['0', '1']:
                    dpa[first_record + last_record] = max(
                        [v for k, v in dp.items() if k[-1] == last_record and k[0] == first_record])
            dp = dpa

        return max(dp.values())

# Runtime: 40 ms, faster than 9.39% of Python3 online submissions for House Robber II.
# Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for House Robber II.

# Time: O(n)
# Space: O(1)