class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        def maxIdx(arr):
            total = 0
            max_idx, larg = 0, arr[0]
            for idx, num in enumerate(arr):
                total += num
                if num > larg:
                    max_idx = idx
                    larg = num
            return max_idx, larg, total

        while True:
            max_idx, larg, total = maxIdx(target)
            if larg == 1:
                return True
            else:
                others = total - larg
                multiplier =  (larg - others) // others
                if multiplier <= 0:
                    multiplier = 1
                target[max_idx] = larg - others * multiplier
                if target[max_idx] < 1:
                    return False

# Time: O(n^2)
# Space: O(1)

# Runtime: 384 ms, faster than 5.11% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 19.9 MB, less than 81.02% of Python3 online submissions for Construct Target Array With Multiple Sums.
