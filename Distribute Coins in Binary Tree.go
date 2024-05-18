/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}
func distributeCoins(root *TreeNode) int {
    var explore func(*TreeNode)(int, int)
    explore = func(node *TreeNode)(int, int) {
        nett := node.Val - 1
        cost := 0
        if node.Left != nil {
            left_nett, left_cost := explore(node.Left)
            cost += left_cost + abs(left_nett)
            nett += left_nett
        }

        if node.Right != nil {
            right_nett, right_cost := explore(node.Right)
            cost += right_cost + abs(right_nett)
            nett += right_nett
        }

        return nett, cost
    }
    _, cost := explore(root)
    return cost
}
