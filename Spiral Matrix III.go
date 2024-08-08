func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
    total := rows * cols - 1
    movement := []int{1,1,2,2}
    direction := 0
    multiplier := [][]int{
        {0,1},
        {1,0},
        {0,-1},
        {-1, 0},
    }
    ans := [][]int{{rStart,cStart}}
    for total > 0 {
        move_x, move_y := multiplier[direction][0], multiplier[direction][1]
        for i := 1; i < movement[direction]+1; i++ {
            rStart += move_x
            cStart += move_y

            if 0 <= rStart && rStart < rows && 0 <= cStart && cStart < cols {
                ans = append(ans, []int{rStart, cStart})
                total--
            }
        }

        movement[direction] += 2
        direction += 1
        direction %= 4
    }
    return ans
}
