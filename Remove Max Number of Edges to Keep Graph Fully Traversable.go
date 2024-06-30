func find(x int, parents *[]int) int {
    if (*parents)[x] != x {
        main_parent := find((*parents)[x], parents)
        (*parents)[x] = main_parent
        return main_parent
    }
    return x
}

func union(x, y int, parents *[]int) int {
    parent_x := find(x, parents)
    parent_y := find(y, parents)
    if parent_x == parent_y {
        return 1
    }

    (*parents)[parent_y] = parent_x
    return 0
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
    parents := make([]int, n)
    for i := 0; i < n; i++ {
        parents[i] = i
    }
    count := 0
    islands := n
    for _, edge := range edges {
        t, u, v := edge[0], edge[1], edge[2]
        if t == 3 {
            inc := union(u-1, v-1, &parents)
            count += inc
            islands -= 1-inc
        }
    }

    parents_2 := append([]int{}, parents...)
    islands2 := islands
    for _, edge := range edges {
        t, u, v := edge[0], edge[1], edge[2]
        if t == 1 {
            inc := union(u-1, v-1, &parents)
            count += inc
            islands -= 1-inc
        } else if t == 2 {
            inc := union(u-1, v-1, &parents_2)
            count += inc
            islands2 -= 1-inc
        }
    }

    if islands2 != 1 || islands != 1 {
        return -1
    }
    return count
}

