import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxx_nums = [-1 * num if num % 2 == 0 else -1 * num*2 for num in nums]
        min_num, max_num = max(maxx_nums), min(maxx_nums)
        min_dev = min_num - max_num
        heapq.heapify(maxx_nums)

        while maxx_nums[0] % 2 == 0:
            new_num = maxx_nums[0] // 2
            min_num = max(min_num, new_num)
            heapq.heapreplace(maxx_nums, new_num)
            min_dev = min(min_dev, min_num - maxx_nums[0])

        return min_dev

# Runtime: 852 ms, faster than 98.29% of Python3 online submissions for Minimize Deviation in Array.
# Memory Usage: 26 MB, less than 93.38% of Python3 online submissions for Minimize Deviation in Array.

# Time: O(n)
# Space: O(n)

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        dp = {}

        def addnum(idx, num):
            if num in dp.keys():
                dp[num].add(idx)
            else:
                dp[num] = set([idx])

        for idx, num in enumerate(nums):
            if num % 2 == 1:
                addnum(idx, 2*num)
                addnum(idx, num)
            else:
                while num % 2 == 0:
                    addnum(idx, num)
                    num = num // 2
                addnum(idx, num)

        current_window = {}
        min_dev = 99999999999
        n = len(nums)
        limit_factor_idx = -1
        check_window_is_filled_once = False
        for i in sorted(list(dp.keys())):
            idxes = dp[i]
            for idx in idxes:
                current_window[idx] = i
            if limit_factor_idx in idxes:
                limit_factor_idx = min(current_window, key=current_window.get)
                min_dev = min(max(current_window.values()) - min(current_window.values()), min_dev)
            if not check_window_is_filled_once and len(current_window) == n:
                limit_factor_idx = min(current_window, key=current_window.get)
                min_dev = min(max(current_window.values()) - min(current_window.values()), min_dev)
                check_window_is_filled_once = True

        return min_dev

# Runtime: 2596 ms, faster than 5.34% of Python3 online submissions for Minimize Deviation in Array.
# Memory Usage: 105.6 MB, less than 5.13% of Python3 online submissions for Minimize Deviation in Array.

# Time: O(n)
# Space: O(n)