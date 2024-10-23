/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func replaceValueInTree(root *TreeNode) *TreeNode {
    summ := make(map[int]map[*TreeNode]int)
    children := make(map[int]map[*TreeNode][]*TreeNode)
    var recur func(node, parent *TreeNode, level int)
    recur = func(node, parent *TreeNode, level int) {
        if node == nil {
            return
        }

        if level == 0 {
            summ[level] = map[*TreeNode]int{
                nil: 0,
            }
            children[level] = map[*TreeNode][]*TreeNode{
                nil: {node},
            }
        } else {
            if _, ok := summ[level]; !ok {
                summ[level] = make(map[*TreeNode]int)
                children[level] = make(map[*TreeNode][]*TreeNode)
            }
            if _, ok := summ[level][parent]; !ok {
                summ[level][parent] = node.Val
                children[level][parent] = []*TreeNode{node}
            } else {
                summ[level][parent] += node.Val
                children[level][parent] = append(children[level][parent], node)
            }
        }
        recur(node.Left, node, level+1)
        recur(node.Right, node, level+1)
    }
    recur(root, nil, 0)
    for level, d := range summ {
        total_count := 0
        for _, count := range d {
            total_count += count
        }

        for parent, count := range d {
            corrected := total_count - count
            for _, node := range children[level][parent] {
                node.Val = corrected
            }
        }
    }
    return root
}
