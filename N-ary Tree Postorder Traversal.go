/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
    if root == nil {
        return []int{}
    }
    arr := []*Node{root}
    ans := make([]int, 0)
    for len(arr) > 0 {
        node := arr[len(arr)-1]
        arr = arr[:len(arr)-1]
        ans = append(ans, node.Val)
        for _, child := range node.Children {
            arr = append(arr, child)
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