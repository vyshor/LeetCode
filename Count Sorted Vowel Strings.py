class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = {(1, i): i for i in range(1, 6)}
        for iter in range(2,n+1):
            for i in range(1, 6):
                dp[(iter, i)] = dp[(iter - 1, i)]  + (dp[(iter, i - 1)] if i > 1 else 0)
        return dp[(n, 5)]

# Runtime: 36 ms, faster than 37.32% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.4 MB, less than 16.32% of Python3 online submissions for Count Sorted Vowel Strings.

# Time: O(5n)
# Space: O(5n)