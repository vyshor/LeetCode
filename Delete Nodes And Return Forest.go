/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    nodes := make([]*TreeNode, 0)
    to_del := make(map[int]interface{})
    dummy := &TreeNode{Left:root}
    for _, d := range to_delete {
        to_del[d] = nil
    }

    var explore func(node *TreeNode, parent *TreeNode, left bool)
    explore = func(node *TreeNode, parent *TreeNode, left bool) {
        if node == nil {
            return
        }

        explore(node.Left, node, true)
        explore(node.Right, node, false)

        if _, ok := to_del[node.Val]; ok {
            if left {
                parent.Left = nil
            } else {
                parent.Right = nil
            }

            if node.Left != nil {
                nodes = append(nodes, node.Left)
            }

            if node.Right != nil {
                nodes = append(nodes, node.Right)
            }
        }
    }

    explore(root, dummy, true)
    if dummy.Left != nil {
        nodes = append(nodes, root)
    }
    return nodes
}

