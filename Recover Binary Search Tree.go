/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func recoverTree(root *TreeNode)  {
    nodes := make([]*TreeNode, 0)
    var recur func(node *TreeNode)
    recur = func(node *TreeNode) {
        if node == nil {
            return
        }

        recur(node.Left)
        nodes = append(nodes, node)
        recur(node.Right)
    }

    recur(root)

    n := len(nodes)
    if n == 2 {
        nodes[0].Val, nodes[1].Val = nodes[1].Val, nodes[0].Val
        return
    }

    var wrongA, wrongB *TreeNode
    for i := 1; i < n; i++ {
        if nodes[i-1].Val > nodes[i].Val {
            wrongA = nodes[i]
        }
    }

    for i := n-2; i > -1; i-- {
        if nodes[i].Val > nodes[i+1].Val {
            wrongB = nodes[i]
        }
    }

    wrongA.Val, wrongB.Val = wrongB.Val, wrongA.Val
}
