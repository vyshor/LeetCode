class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1 = 0
        max2 = 0
        for idx
        max_vol = 0
        for idx, x in enumerate(height):
            for idx2, y in enumerate(height[idx+1:]):
                z = min(x,y)
                vol = (idx2+1)*z
                if vol > max_vol:
                    max_vol = vol
        return max_vol

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0
        while l != r:
            h = min(height[l], height[r])
            vol = (r-l)*h
            if vol > max_vol:
                max_vol = vol
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_vol

# Time: O(n)
# Space: O(1)
# Runtime: 144 ms, faster than 66.15% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.5 MB, less than 5.26% of Python3 online submissions for Container With Most Water.