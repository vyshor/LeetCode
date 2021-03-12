from collections import deque
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        seen = set()
        end_pt = k-1
        total_comb = 0
        sliding_window = deque(list(s[:end_pt]))
        while end_pt < len(s):
            sliding_window.append(s[end_pt])
            hashable = tuple(sliding_window)
            if hashable not in seen:
                seen.add(hashable)
                total_comb += 1
            sliding_window.popleft()
            end_pt += 1
        return total_comb == 2**k

# Time: O(n)
# Space: O(2**n)

# Runtime: 816 ms, faster than 19.41% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Memory Usage: 43 MB, less than 9.28% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
