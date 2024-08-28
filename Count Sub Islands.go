func key(i, j int) int {
    return i << 10 | j
}

type Point struct {
    i int
    j int
}

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
    n := len(grid2)
    m := len(grid2[0])
    visited := make(map[int]interface{})
    islands := 0

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            k := key(i, j)
            if _, ok := visited[k]; ok || grid2[i][j] == 0 {
                continue
            }

            q := []Point{{i: i, j:j}}
            is_island := true
            for len(q) > 0 {
                point := q[len(q)-1]
                q = q[:len(q)-1]
                x, y := point.i, point.j
                k2 := key(x, y)
                if _, ok := visited[k2]; ok {
                    continue
                }
                visited[k2] = nil
                if grid1[x][y] == 0 {
                    is_island = false
                }

                dirs := []Point{
                    {x-1, y},
                    {x+1, y},
                    {x, y-1},
                    {x, y+1},
                }
                for _, dir := range dirs {
                    if dir.i >= n || dir.i < 0 || dir.j >= m || dir.j < 0 || grid2[dir.i][dir.j] == 0 {
                        continue
                    }
                    q = append(q, dir)
                }
            }
            if is_island {
                islands++
            }
        }
    }
    return islands
}
