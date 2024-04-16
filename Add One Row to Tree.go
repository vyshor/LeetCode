/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if depth == 1 {
        return &TreeNode{Val:val, Left:root}
    }

    var exploreNode func(*TreeNode, int)
    exploreNode = func(node *TreeNode, d int) {
        if node == nil {
            return
        }

        if d == 1 {
            node.Left = &TreeNode{Val:val, Left:node.Left}
            node.Right = &TreeNode{Val:val, Right:node.Right}
        }

        exploreNode(node.Left, d-1)
        exploreNode(node.Right, d-1)
    }

    exploreNode(root, depth-1)
    return root
}
