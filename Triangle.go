func minimumTotal(triangle [][]int) int {
    h := len(triangle)
    for i := 1; i < h; i++ {
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
        for j := 1; j < i; j++ {
            triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        }
    }
    return slices.Min(triangle[h-1])
}