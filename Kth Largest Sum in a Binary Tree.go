/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargestLevelSum(root *TreeNode, k int) int64 {
    summ := make([]int64, 0)
    var recur func(*TreeNode, int)
    recur = func(node *TreeNode, level int) {
        if node == nil {
            return
        }

        if len(summ) == level {
            summ = append(summ, int64(node.Val))
        } else {
            summ[level] += int64(node.Val)
        }
        recur(node.Left, level+1)
        recur(node.Right, level+1)
    }
    recur(root, 0)
    if len(summ) < k {
        return -1
    }
    sort.Slice(summ, func(i, j int) bool {return summ[i] > summ[j]})
    return summ[k-1]
}

