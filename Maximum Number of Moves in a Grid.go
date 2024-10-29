func maxMoves(grid [][]int) int {
    dp := make(map[int]int)
    n := len(grid)
    m := len(grid[0])
    var recur func(i, j int) int
    recur = func(i, j int) int {
        key := (i << 10 | j)
        if val, ok := dp[key]; ok {
            return val
        }

        if j == m {
            return 0
        }

        if j+1 == m {
            return 1
        }

        moves := 0
        val := grid[i][j]
        if grid[i][j+1] > val {
            moves = max(moves, recur(i, j+1))
        }
        if i-1 >= 0 && grid[i-1][j+1] > val {
            moves = max(moves, recur(i-1, j+1))
        }
        if i+1 < n && grid[i+1][j+1] > val {
            moves = max(moves, recur(i+1, j+1))
        }
        dp[key] = moves+1
        return moves+1
    }

    maxx := 0
    for i := 0; i < n; i++ {
        maxx = max(maxx, recur(i, 0))
    }
    return maxx-1
}
