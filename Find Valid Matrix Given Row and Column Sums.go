func restoreMatrix(rowSum []int, colSum []int) [][]int {
    n := len(rowSum)
    m := len(colSum)
    matrix := make([][]int, 0)
    for i := 0; i < n; i++ {
        arr := make([]int, m)
        matrix = append(matrix, arr)
    }

    i := 0
    j := 0
    for i < n && j < m {
        matrix[i][j] =  min(rowSum[i], colSum[j])
        rowSum[i] -= matrix[i][j]
        colSum[j] -= matrix[i][j]
        for i < n && rowSum[i] == 0 {
            i++
        }

        for j < m && colSum[j] == 0 {
            j++
        }
    }
    return matrix
}
