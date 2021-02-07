# Two pointers, start and end
# End pointer will move until there is a similar char
# If there is similar char, check all count <= 0
# If all count <= 0, set min_len if possible
# If start_char < 0,
# Move start to next valid char
#
# ADOBECODEBANC
# A  B C   B
# A  B C   BA
#      C   BA
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_wdw = {}
        for c in t:
            try:
                char_wdw[c] += 1
            except KeyError:
                char_wdw[c] = 1

        start, end = 0, -1
        min_len = len(s) + 1
        ans_s = 0
        ans_e = -1
        while end < len(s) - 1:
            end += 1
            try:
                char_wdw[s[end]] -= 1
                if all([x <= 0 for x in char_wdw.values()]):
                    if min_len > end - start + 1:
                        min_len = end - start + 1
                        ans_s = start
                        ans_e = end
                valid = start
                while 1:
                    try:
                        char_wdw[s[valid]]
                        if char_wdw[s[valid]] < 0:
                            char_wdw[s[valid]] += 1
                            start = valid
                            if all([x <= 0 for x in char_wdw.values()]):
                                if min_len > end - start + 1:
                                    min_len = end - start + 1
                                    ans_s = start
                                    ans_e = end
                            valid += 1
                        else:
                            start = valid
                            if all([x <= 0 for x in char_wdw.values()]):
                                if min_len > end - start + 1:
                                    min_len = end - start + 1
                                    ans_s = start
                                    ans_e = end
                            break
                    except KeyError:
                        valid += 1
            except KeyError:
                pass
        return s[ans_s:ans_e + 1]

# Time: O(n)
# Space: O(k)
# Runtime: 672 ms, faster than 6.94% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.6 MB, less than 5.55% of Python3 online submissions for Minimum Window Substring.