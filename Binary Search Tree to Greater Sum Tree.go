/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func bstToGst(root *TreeNode) *TreeNode {
    var check func(node *TreeNode, summ int) int
    check = func(node *TreeNode, summ int) int {
        if node == nil {
            return summ
        }

        summ = check(node.Right, summ)
        summ += node.Val
        node.Val = summ
        return check(node.Left, summ)
    }
    check(root, 0)
    return root
}
