func minFallingPathSum(matrix [][]int) int {
    n := len(matrix)
    m := len(matrix[0])
    for i := 1; i < n; i++ {
        for j := 0; j < m; j++ {
            cost := matrix[i-1][j]
            if j > 0 {
                cost = min(cost, matrix[i-1][j-1])
            }
            if j < m-1 {
                cost = min(cost, matrix[i-1][j+1])
            }
            matrix[i][j] += cost
        }
    }
    val := matrix[n-1][0]
    for _, v := range matrix[n-1] {
        val = min(val, v)
    }
    return val
}
