/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type ParentNode struct {
    Parent *TreeNode
    Left bool
}

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    parents := make(map[*TreeNode]*ParentNode)
    dummy := &TreeNode{Left:root}
    var explore func(*TreeNode)
    explore = func(node *TreeNode) {
        if node.Left == nil && node.Right == nil && node.Val == target {
            parent_node := parents[node]
            parent := parent_node.Parent
            if parent_node.Left {
                parent.Left = nil
            } else {
                parent.Right = nil
            }
            delete(parents, node)
            explore(parent)
        }

        if node.Left != nil {
            parents[node.Left] = &ParentNode{Parent: node, Left: true}
            explore(node.Left)
        }

        if node.Right != nil {
            parents[node.Right] = &ParentNode{Parent: node, Left: false}
            explore(node.Right)
        }
    }

    explore(dummy)
    return dummy.Left
}
