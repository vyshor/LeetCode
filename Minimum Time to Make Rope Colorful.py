class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        prev_color, prev_time = colors[0], neededTime[0]
        min_time = 0
        for i in range(1, n):
            if colors[i] == prev_color:
                min_time += min(prev_time, neededTime[i])
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_color = colors[i]
                prev_time = neededTime[i]
        return min_time
