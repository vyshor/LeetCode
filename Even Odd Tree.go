/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isEvenOddTree(root *TreeNode) bool {
    levels := make([][]int, 0)
    var exploreNode func(node *TreeNode, depth int) bool
    exploreNode = func(node *TreeNode, depth int) bool {
        if node == nil {
            return true
        }

        if len(levels) == depth {
            arr := make([]int, 0)
            levels = append(levels, arr)
        }

        if len(levels[depth]) > 0 {
            last_num := levels[depth][len(levels[depth])-1]
            if depth & 1 == 1 {
                if last_num <= node.Val {
                    return false
                }
            } else {
                if last_num >= node.Val {
                    return false
                }
            }
        }

        if depth & 1 == 1 {
            if node.Val & 1 == 1 {
                return false
            }
        } else {
            if node.Val & 1 == 0 {
                return false
            }
        }

        levels[depth] = append(levels[depth], node.Val)
        return exploreNode(node.Left, depth+1) && exploreNode(node.Right, depth+1)
    }
    return exploreNode(root, 0)
}
