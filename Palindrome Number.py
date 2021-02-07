class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == ''.join(reversed(str(x)))

# Time: O(n) for length n of string
# Space: O(n) for length n of string
# Runtime: 68 ms, faster than 38.19% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
