/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
    var recur func(node1, node2 *TreeNode) bool
    recur = func(node1, node2 *TreeNode) bool {
        switch {
            case node1 == nil && node2 == nil:
            return true
            case node1 == nil || node2 == nil:
            return false
            case node1.Val != node2.Val:
            return false
            case node1.Left == nil && node2.Right == nil:
            return recur(node1.Right, node2.Left)
            case node1.Right == nil && node2.Left == nil:
            return recur(node1.Left, node2.Right)
            case node1.Left != nil && node2.Left != nil && node1.Left.Val != node2.Left.Val:
            return recur(node1.Left, node2.Right) && recur(node1.Right, node2.Left)
            default:
            return recur(node1.Left, node2.Left) && recur(node1.Right, node2.Right)
        }
    }
    return recur(root1, root2)
}
