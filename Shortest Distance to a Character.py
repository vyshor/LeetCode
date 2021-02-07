class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist = []
        stack = []
        prev_c_loc = -1
        max_dist = len(s)
        for idx, s_char in enumerate(s):
            if s_char != c:
                stack.append(idx)
                if prev_c_loc != -1:
                    dist.append(idx - prev_c_loc)
                else:
                    dist.append(max_dist)
            else:
                dist.append(0)
                i = 1
                while len(stack):
                    prev_idx = stack.pop()
                    dist[prev_idx] = min(i, dist[prev_idx])
                    i += 1
                prev_c_loc = idx
        return dist

# Time: O(n)
# Space: O(n)

# Runtime: 44 ms, faster than 61.94% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 14.5 MB, less than 32.19% of Python3 online submissions for Shortest Distance to a Character.