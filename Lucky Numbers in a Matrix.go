func luckyNumbers (matrix [][]int) []int {
    n := len(matrix)
    m := len(matrix[0])
    rows := make([]int, n)
    cols := make([]int, m)
    for i := range n {
        for j := range m {
            if rows[i] == 0 {
                rows[i] = matrix[i][j]
            } else {
                rows[i] = min(rows[i], matrix[i][j])
            }
            cols[j] = max(cols[j], matrix[i][j])
        }
    }

    cols_set := make(map[int]interface{})
    for _, num := range cols {
        cols_set[num] = nil
    }
    ans := make([]int, 0)
    for i := range n {
        if _, ok := cols_set[rows[i]]; ok {
            ans = append(ans, rows[i])
        }
    }
    return ans
}

