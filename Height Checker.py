class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = list(heights)
        new_heights.sort()
        count = 0
        for i in range(len(heights)):
            count += int(heights[i] != new_heights[i])
        return count
