func validPath(n int, edges [][]int, source int, destination int) bool {
    if source == destination {
        return true
    }

    paths := make(map[int][]int)
    for _, edge := range edges {
        u := edge[0]
        v := edge[1]
        if _, ok :=paths[u]; !ok {
            paths[u] = []int{v}
        } else {
            paths[u] = append(paths[u], v)
        }

        if _, ok := paths[v]; !ok {
            paths[v] = []int{u}
        } else {
            paths[v] = append(paths[v], u)
        }
    }

    j := 0
    q := []int{source}
    visited := make(map[int]interface{})
    visited[source] = nil

    for (j < len(q)) {
        i := q[j]

        fmt.Println(j, i, q)
        j++

        if _, ok := paths[i]; !ok {
            continue
        }

        for _, dst := range paths[i] {
            if _, ok := visited[dst]; ok {
                continue
            }

            if dst == destination {
                return true
            }

            q = append(q, dst)
            visited[dst] = nil
        }
    }
    return false
}

