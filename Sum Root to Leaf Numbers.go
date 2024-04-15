/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var summ int
func exploreNode(node *TreeNode, path string) {
    if node == nil {
        return
    }

    path += strconv.Itoa(node.Val)

    if node.Left == nil && node.Right == nil {
        i, _ := strconv.Atoi(path)
        summ += i
        return
    }

    exploreNode(node.Left, path)
    exploreNode(node.Right, path)
}

func sumNumbers(root *TreeNode) int {
    summ = 0
    exploreNode(root, "")
    return summ
}
