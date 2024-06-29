func add(dst, src map[int]interface{}) {
    for v := range src {
        dst[v] = nil
    }
}

func convert(m map[int]interface{}) []int {
    l := make([]int, len(m))
    i := 0
    for v := range m {
        l[i] = v
        i++
    }
    sort.Ints(l)
    return l
}

func getAncestors(n int, edges [][]int) [][]int {
    q := make([]int, 0)
    in_edges := make([]int, n)
    pairs := make(map[int][]int)
    for _, edge := range edges {
        pairs[edge[0]] = append(pairs[edge[0]], edge[1])
        in_edges[edge[1]]++
    }

    for i, in_count := range in_edges {
        if in_count == 0 {
            q = append(q, i)
        }
    }

    ans := make([]map[int]interface{}, n)
    for i := 0; i < n; i++ {
        ans[i] = make(map[int]interface{})
    }

    for len(q) > 0 {
        i := q[len(q)-1]
        q = q[:len(q)-1]
        if targets, ok := pairs[i]; ok {
            for _, target := range targets {
                ans[target][i] = nil
                add(ans[target], ans[i])
                in_edges[target]--
                if in_edges[target] == 0 {
                    q = append(q, target)
                }
            }
        }
    }

    sorted_ans := make([][]int, n)
    for i := 0; i < n; i++ {
        sorted_ans[i] = convert(ans[i])
    }
    return sorted_ans
}
