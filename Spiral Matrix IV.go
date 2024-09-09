/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func spiralMatrix(m int, n int, head *ListNode) [][]int {
    matrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            matrix[i][j] = -1
        }
    }

    i := 0
    j := -1
    dirs := [][]int{
        {0, 1},
        {1, 0},
        {0, -1},
        {-1, 0},
    }

    direct := 0
    ptr := head
    delta_x := 0
    delta_y := 1
    for ptr != nil {
        if i+delta_x < 0 || i+delta_x >= m || j+delta_y < 0 || j+delta_y >= n || matrix[i+delta_x][j+delta_y] != -1 {
            direct++
            direct %= 4

            delta_x = dirs[direct][0]
            delta_y = dirs[direct][1]
        }

        i += delta_x
        j += delta_y
        matrix[i][j] = ptr.Val
        ptr = ptr.Next
    }
    return matrix
}
