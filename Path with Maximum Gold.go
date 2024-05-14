func getMaximumGold(grid [][]int) int {
    n := int64(len(grid))
    m := int64(len(grid[0]))
    gold_pos := make(map[int64]int64)
    dp := make(map[int64]int)
    maxx := 0

    k := 0
    for i := int64(0); i < n; i++ {
        for j := int64(0); j < m; j++ {
            if grid[i][j] > 0 {
                gold_pos[(i << 16) | j] = (1 << k)
                k++
            }
        }
    }

    var explore func(i, j, state int64) int
    explore = func(i, j, state int64) int {
        state |= gold_pos[(i << 16) | j]

        key := (i << 48) | (j << 32) | state
        if val, ok := dp[key]; ok {
            return val
        }

        val := grid[i][j]
        maxx_move := 0
        arr := [][]int64{
            {i-1, j},
            {i+1, j},
            {i, j-1},
            {i, j+1},
        }

        for _, arr_val := range arr {
            x := arr_val[0]
            y := arr_val[1]

            if 0 <= x && x < n && 0 <= y && y < m && grid[x][y] > 0 && (gold_pos[(x << 16) | y] & state == 0) {
                maxx_move = max(maxx_move, explore(x, y, state))
            }
        }

        val += maxx_move
        dp[key] = val
        maxx = max(maxx, val)
        return val
    }

    for i := int64(0); i < n; i++ {
        for j := int64(0); j < m; j++ {
            if grid[i][j] > 0 {
                explore(i, j, 0)
            }
        }
    }
    return maxx
}
