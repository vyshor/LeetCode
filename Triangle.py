class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        for i in range(1, h):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[h-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
