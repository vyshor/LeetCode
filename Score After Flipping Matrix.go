func matrixScore(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])
    for i := 0; i < n; i++ {
        if grid[i][0] == 0 {
            for j := 0; j < m; j++ {
                grid[i][j] ^= 1
            }
        }
    }

    count := n * ( 1 << (m-1))
    for j := 1; j < m; j++ {
        current_count := 0
        for i := 0; i < n; i++ {
            current_count += grid[i][j]
        }
        count += (1 << (m-1-j)) * max(current_count, n-current_count)
    }
    return count
}