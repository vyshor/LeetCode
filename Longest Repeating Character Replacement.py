# AABBAABB
# AABB
# AABBA
# AABBAA
# BBAAB


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        start, end = 0, k - 1
        most_char, most_count = '', 0
        fill_size = {'total': 0}
        sliding_wdw = s[start:end + 1]
        start_char = s[start]
        for x in sliding_wdw:
            if x not in fill_size:
                fill_size[x] = 1
            else:
                fill_size[x] += 1
            fill_size['total'] += 1
            if fill_size[x] > most_count:
                most_char = x
                most_count = fill_size[x]
        n = len(s)
        max_char = fill_size['total']
        while end < n - 1:
            end += 1
            fill_size['total'] += 1
            try:
                fill_size[s[end]] += 1
            except KeyError:
                fill_size[s[end]] = 1
            if fill_size[s[end]] > most_count:
                most_char = s[end]
                most_count = fill_size[s[end]]
            if fill_size[
                'total'] - most_count > k:  # If it is not repeating, check if fill_size + 1 > k, it means the sliding window needs to scale down
                # Iterate through the starting until it matches the end
                fill_size[s[start]] -= 1
                fill_size['total'] -= 1
                start += 1

            curr_fill_size = fill_size['total']
            if max_char < curr_fill_size:
                max_char = curr_fill_size
        return max_char

# Time: O(n)
# Space: O(n)
# Runtime: 96 ms, faster than 97.43% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 13.9 MB, less than 12.50% of Python3 online submissions for Longest Repeating Character Replacement.