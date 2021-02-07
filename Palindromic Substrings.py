# Start, mid, end
# Every iteration
# End, and mid will move
#

# abbaa
# <>abbaa
# <a>bbaa
# <a|b>baa
# <abb>aa
# <ab|ba>a
# <abbaa>
# a<bb|aa>
# ab<baa>

class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '$#' + '#'.join(list(s)) + '#@'
        i, c, r, mir = 1, 1, 1, 1
        n = len(s)
        pal_count = 0
        pal = [0] * n
        while i < n - 1:
            mir = 2 * c - i

            if i < r:
                pal[i] = min(r - i, pal[mir])

            while s[i - pal[i] - 1] == s[i + pal[i] + 1]:
                pal[i] += 1

            if i + pal[i] > r:
                c = i
                r = c + pal[i]

            if pal[i]:
                pal_count += (pal[i] + 1) // 2
            i += 1
        return pal_count

# Manacher's Algorithm
# Time: O(n)
# Space: O(n)
# Runtime: 44 ms, faster than 97.91% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Palindromic Substrings.
