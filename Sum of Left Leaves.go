/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    var summ int
    var exploreNode func(*TreeNode, bool)
    exploreNode = func(node *TreeNode, is_left bool) {
        if node == nil {
            return
        }

        if node.Left == nil && node.Right == nil && is_left {
            summ += node.Val
        }

        exploreNode(node.Left, true)
        exploreNode(node.Right, false)
    }
    exploreNode(root, false)
    return summ
}
