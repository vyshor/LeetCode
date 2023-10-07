class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        dp = {}

        def getCost(points, start, end):
            str_points = str(points)
            if (str_points, start, end) in dp:
                return dp[(str_points, start, end)]

            if len(points) == 0:
                dp[(str_points, start, end)] = 0
                return dp[(str_points, start, end)]

            base_cost = end - start
            extra_cost = float('inf')
            for i, cutPoint in enumerate(points):
                extra_cost = min(extra_cost,
                                 getCost(points[:i], start, cutPoint) + getCost(points[i + 1:], cutPoint, end))

            dp[(str_points, start, end)] = base_cost + extra_cost
            return dp[(str_points, start, end)]

        total_cost = getCost(cuts, 0, n)
        # print(dp)
        return total_cost
