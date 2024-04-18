func islandPerimeter(grid [][]int) int {
    var perimeter int
    n := len(grid)
    m := len(grid[0])

    for i := 0; i < n; i++ {
        prev := 0
        for j := 0; j < m; j++ {
            perimeter += grid[i][j] ^ prev
            prev = grid[i][j]
        }
        perimeter += prev
    }


    for j := 0; j < m; j++ {
        prev := 0
        for i := 0; i < n; i++ {
            perimeter += grid[i][j] ^ prev
            prev = grid[i][j]
        }
        perimeter += prev
    }

    return perimeter
}


// func getKey(i, j int) int {
//     return (i << 10) | j
// }
//
// func returnKey(key int) (int, int) {
//     i := key >> 10
//     j := ((1 << 10) - 1) & key
//     return i, j
// }
//
// func islandPerimeter(grid [][]int) int {
//     visited := make(map[int]interface{})
//     var perimeter int
//     n := len(grid)
//     m := len(grid[0])
//     q := make([]int, 0)
//
//     to_break := false
//     for i := 0; i < n; i++ {
//         for j := 0; j < m; j++ {
//             if grid[i][j] == 1 {
//                 key := getKey(i, j)
//                 q = append(q, key)
//                 to_break = true
//                 break
//             }
//         }
//
//         if to_break {
//             break
//         }
//     }
//
//     for len(q) > 0 {
//         key := q[len(q)-1]
//         q = q[:len(q)-1]
//         if _, ok := visited[key]; ok {
//             continue
//         }
//
//         visited[key] = nil
//         i, j := returnKey(key)
//         keys := []int{getKey(i-1, j), getKey(i+1, j), getKey(i, j-1), getKey(i, j+1)}
//         for _, new_key := range keys {
//             if _, ok := visited[new_key]; ok {
//                 continue
//             }
//             x, y := returnKey(new_key)
//             if 0 <= x && x < n && 0 <= y && y < m && grid[x][y] == 1 {
//                 q = append(q, new_key)
//             } else {
//                 perimeter++
//             }
//         }
//
//     }
//     return perimeter
// }

