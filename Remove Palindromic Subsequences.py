class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2

# Time: O(n)
# Space: O(1)

# Runtime: 32 ms, faster than 58.63% of Python3 online submissions for Remove Palindromic Subsequences.
# Memory Usage: 14.1 MB, less than 90.00% of Python3 online submissions for Remove Palindromic Subsequences.
