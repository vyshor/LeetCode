class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dp = {}
        for (w, h) in rectangles:
            grad = w / h
            if grad not in dp:
                dp[grad] = 1
            else:
                dp[grad] += 1

        count = 0
        for rects in dp.values():
            count += rects * (rects - 1) // 2
        return count
