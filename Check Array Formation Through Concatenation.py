class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dp = {}
        dp_solved = {}

        for idx, num in enumerate(arr):
            dp[num] = idx

        for piece in pieces:
            if not (type(dp.get(piece[0])) == int):
                continue
            idx_ref = dp[piece[0]]
            for idx, num in enumerate(piece):
                if not (type(dp.get(num)) == int):
                    continue
                dp_solved[num] = True
                if idx_ref + idx != dp[num]:
                    return False
        return len(dp) == len(dp_solved)

# Runtime: 44 ms, faster than 43.86% of Python3 online submissions for Check Array Formation Through Concatenation.
# Memory Usage: 14.3 MB, less than 60.20% of Python3 online submissions for Check Array Formation Through Concatenation.

# Time: O(n+m) for n integers in arr and m integers in pieces
# Space: O(n) for n integers in arr