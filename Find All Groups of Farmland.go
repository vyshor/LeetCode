func findFarmland(land [][]int) [][]int {
    n := len(land)
    m := len(land[0])
    ans := make([][]int, 0)
    jumps := make(map[int]int)

    i := 0
    for i < n {
        j := 0
        for j < m {
            if land[i][j] == 1 {
                key := (i << 10) | j
                if new_pos, ok := jumps[key]; ok {
                    j = new_pos
                    continue
                } else {
                    x := i
                    y := j
                    for y+1 < m && land[x][y+1] == 1{
                        y++
                    }

                    for x+1 < n && land[x+1][y] == 1 {
                        x++
                    }

                    ans = append(ans, []int{i, j, x, y})
                    for k := i+1; k <= x; k++ {
                        jumps[(k << 10) | j] = y+1
                    }
                    j = y
                }
            }
            j++
        }
        i++
    }
    return ans
}
