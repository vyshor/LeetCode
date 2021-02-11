from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time: O(n+m)
# Space: O(n+m)

# Runtime: 32 ms, faster than 98.22% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 48.96% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for c in s:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1

        for c in t:
            if c not in h:
                return False
            else:
                h[c] -= 1
                if h[c] < 0:
                    return False
        return not any(h.values())


# Time: O(s+t) = O(2s) since terminates if any value hits below zero = O(s)
# Space: O(m) where m = max(s,t)
# Runtime: 56 ms, faster than 69.71% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.1 MB, less than 9.38% of Python3 online submissions for Valid Anagram.
