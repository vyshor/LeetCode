class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s =   '$#' + '#'.join(list(s)) + '#@'
        longest_pal = 0
        longest_pal_str = ''
        arr = [0]* len(s)
        c, r = 0, 0
        for idx in range(len(s)):
            mirror = 2*c - idx

            if idx < mirror:
                arr[idx] = max(r - idx, arr[mirror])

            while idx - arr[idx] - 1 >= 0 and idx + arr[idx] + 1 < len(s) and s[idx - (arr[idx] + 1)] == s[idx + (arr[idx] + 1)]:
                arr[idx] += 1

            if arr[idx] > longest_pal:
                longest_pal = arr[idx]
                longest_pal_str = s[idx-arr[idx]:idx+arr[idx]+1]

            if idx + arr[idx] > r:
                c = idx
                r = idx + arr[idx]
        return longest_pal_str.replace('#', '')

# Runtime: 3832 ms, faster than 28.24% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.4 MB, less than 39.60% of Python3 online submissions for Longest Palindromic Substring.

# Time: O(n)
# Space: O(n)