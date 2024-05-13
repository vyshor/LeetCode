/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {

    var compareTree func(a, b *TreeNode) bool
    compareTree = func(a,b *TreeNode) bool {
        if a == nil && b == nil {
            return true
        }

        if a == nil || b == nil {
            return false
        }

        if a.Val != b.Val {
            return false
        }

        return compareTree(a.Left, b.Left) && compareTree(a.Right, b.Right)
    }
    return compareTree(p, q)
}
