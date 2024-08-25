/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func postorderTraversal(root *TreeNode) []int {
    arr := []*TreeNode{root}
    ans := make([]int, 0)
    for len(arr) > 0 {
        node := arr[len(arr)-1]
        arr = arr[:len(arr)-1]
        if node != nil {
            ans = append(ans, node.Val)
            arr = append(arr, node.Left)
            arr = append(arr, node.Right)
        }
    }
    n := len(ans) - 1
    i := 0
    for i < n {
        ans[i], ans[n] = ans[n], ans[i]
        i++
        n--
    }
    return ans
}
