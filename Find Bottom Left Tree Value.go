/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
    max_depth := 0
    val := root.Val
    var exploreNode func(node *TreeNode, depth int)

    exploreNode = func(node *TreeNode, depth int) {
        if node == nil {
            return
        }

        if depth > max_depth {
            max_depth = depth
            val = node.Val
        }

        exploreNode(node.Left, depth+1)
        exploreNode(node.Right, depth+1)
    }

    exploreNode(root, 0)
    return val
}
