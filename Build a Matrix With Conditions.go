func condSort(conds [][]int, k int) map[int]int {
    in_edges := make([]int, k)
    edges := make(map[int]map[int]interface{})
    for _, p := range conds {
        fro, to := p[0], p[1]
        fro--
        to--
        if _, ok := edges[fro]; !ok {
            edges[fro] = make(map[int]interface{})
        }

        if _, ok := edges[fro][to]; !ok {
            edges[fro][to] = nil
            in_edges[to]++
        }
    }

    q := make([]int, 0)
    for i := 0; i < k; i++ {
        if in_edges[i] == 0 {
            q = append(q, i)
        }
    }

    order := make([]int, 0)
    for len(q) > 0 {
        i := q[len(q)-1]
        q = q[:len(q)-1]
        order = append(order, i)

        if edges_, ok := edges[i]; ok {
            for j := range edges_ {
                in_edges[j]--
                if in_edges[j] == 0 {
                    q = append(q, j)
                }
            }
        }
    }

    if len(order) < k {
        return nil
    }

    dp := make(map[int]int)
    for i := 0; i < k; i++ {
        dp[order[i]] = i
    }
    return dp
}

func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
    row := condSort(rowConditions, k)
    col := condSort(colConditions, k)
    if row == nil || col == nil {
        return [][]int{}
    }

    matrix := make([][]int, 0)
    for i := 0; i < k; i++ {
        arr := make([]int, k)
        matrix = append(matrix, arr)
    }

    for i := 0; i < k; i++ {
        matrix[row[i]][col[i]] = i+1
    }
    return matrix
}

