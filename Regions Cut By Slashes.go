func regionsBySlashes(grid []string) int {
    n := len(grid)
    islands := (n*n) << 2
    parents := make([]int, islands)
    for i := range islands {
        parents[i] = i
    }

    var find func(i int) int
    find = func(i int) int {
        if parents[i] == i {
            return i
        }

        new_parent := find(parents[i])
        parents[i] = new_parent
        return new_parent
    }

    union := func(i, j int) {
        if i < 0 || i >= len(parents) || j < 0 || j >= len(parents) {
            return
        }

        parent_i := find(i)
        parent_j := find(j)
        if parent_i != parent_j {
            islands--
            parents[parent_j] = parent_i
        }
    }

    get_pos := func(i, j, dir int) int {
        return ((i * n + j) << 2) + dir
    }

    for i := range n {
        for j, c := range grid[i] {
            pos := get_pos(i, j, 0)
            if c == '/' {
                union(pos, get_pos(i, j, 3))
                union(pos, get_pos(i-1, j, 2))
                if j != 0 {
                    union(pos, get_pos(i, j-1, 1))
                }
                union(pos+1, pos+2)
                union(pos+2, get_pos(i+1, j, 0))
                if j != n-1 {
                    union(pos+1, get_pos(i, j+1, 3))
                }
            } else if c == '\\' {
                union(pos, pos + 1)
                union(pos, get_pos(i-1, j, 2))
                if j != n-1 {
                    union(pos, get_pos(i, j+1, 3))
                }

                union(pos+2, pos + 3)
                union(pos+2, get_pos(i+1, j, 0))
                if j != 0 {
                    union(pos+3, get_pos(i, j-1, 1))
                }
            } else {
                union(pos, pos + 1)
                union(pos, pos + 2)
                union(pos, pos + 3)
                union(pos, get_pos(i-1, j, 2))
                union(pos, get_pos(i+1, j, 0))
                if j != 0 {
                    union(pos, get_pos(i, j-1, 1))
                }
                if j != n-1 {
                    union(pos, get_pos(i, j+1, 3))
                }
            }
        }
    }

    return islands
}
