class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True

        (x, y) = coordinates[0]
        (x2, y2) = coordinates[1]

        if y == y2:
            return all([coordinate[1] == y for coordinate in coordinates])

        if x == x2:
            return all([coordinate[0] == x for coordinate in coordinates])

        grad = (y2 - y) / (x2 - x)
        for i in range(2, n):
            (x3, y3) = coordinates[i]
            if (x3 - x) == 0 or grad != (y3 - y) / (x3 - x):
                return False

        return True
