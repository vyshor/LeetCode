/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getDirections(root *TreeNode, startValue int, destValue int) string {
    path := make([]rune, 0)
    var start_path, dest_path string
    var explore func(node *TreeNode)
    explore = func(node *TreeNode) {
        if node == nil {
            return
        }

        if node.Val == startValue {
            start_path = string(path)
        }

        if node.Val == destValue {
            dest_path = string(path)
        }

        path = append(path, 'L')
        explore(node.Left)
        path = path[:len(path)-1]

        path = append(path, 'R')
        explore(node.Right)
        path = path[:len(path)-1]
    }

    explore(root)
    n1 := min(len(start_path), len(dest_path))
    i := 0
    for i < n1 {
        if start_path[i] == dest_path[i] {
            i++
        } else {
            break
        }
    }

    final_path := strings.Repeat("U", len(start_path)-i) + dest_path[i:]
    return final_path
}

