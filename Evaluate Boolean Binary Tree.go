/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    var explore func(node *TreeNode) bool
    explore = func(node *TreeNode) bool {
        if node.Left == nil && node.Right == nil {
            return node.Val == 1
        } else if node.Val == 2 {
            return explore(node.Left) || explore(node.Right)
        } else {
            return explore(node.Left) && explore(node.Right)
        }
    }
    return explore(root)
}
