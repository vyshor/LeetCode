class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, -1
        n = len(s)
        max_len = 0
        str_len = 0
        char_wdw = {}
        while end < n - 1:
            end += 1
            str_len += 1
            try:
                char_wdw[s[end]]  # That means there is existing
                new_start = char_wdw[s[end]] + 1
                while start < new_start:
                    del char_wdw[s[start]]
                    str_len -= 1
                    start += 1
            except KeyError:
                pass
            char_wdw[s[end]] = end

            if max_len < str_len:
                max_len = str_len
        return max_len

# Time: O(n)
# Space: O(n)
# Runtime: 72 ms, faster than 56.92% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        max_len = 0
        w_size = 0
        tail = 0
        for idx, c in enumerate(s):
            if not dp.get(c):
                dp[c] = 1
            else:
                dp[c] += 1
                while (dp.get(c) > 1):
                    dp[s[tail]] -= 1
                    tail += 1
            w_size = idx - tail + 1
            max_len = max(w_size, max_len)
        return max_len

# Time: O(n)
# Space: O(n)
# Runtime: 76 ms, faster than 37.64% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.5 MB, less than 23.13% of Python3 online submissions for Longest Substring Without Repeating Characters.