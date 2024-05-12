func largestLocal(grid [][]int) [][]int {
    n := len(grid)
    new_grid := make([][]int, n-2)
    for i := 0; i < n-2; i++ {
        new_grid[i] = make([]int, n-2)
    }

    for i :=0; i< n; i++ {
        for j := 0; j < n; j++ {
            for i2 := i-1; i2 < i+2; i2++ {
                for j2 := j-1; j2 < j+2; j2++ {
                    if 1 <= i2 && i2 < n-1 && 1 <= j2 && j2 < n-1 {
                        new_grid[i2-1][j2-1] = max(new_grid[i2-1][j2-1], grid[i][j])
                    }
                }
            }
        }
    }

    return new_grid
}

