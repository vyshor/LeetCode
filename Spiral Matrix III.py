class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols - 1
        movement = [1, 1, 2, 2]
        direction = 0
        multiplier = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = [[rStart, cStart]]
        while total:
            move_x, move_y = multiplier[direction]
            for i in range(1, movement[direction] + 1):
                rStart += move_x
                cStart += move_y

                # print("Coordinate:", rStart, cStart)
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    total -= 1
                    # print(ans)
                    # print(total)

            movement[direction] += 2
            direction += 1
            direction %= 4
        return ans

