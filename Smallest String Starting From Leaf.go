/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func compare(a []int, b []int) bool {
    n1 := len(a)-1
    n2 := len(b)-1

    for {
        if n1 == -1 {
            return true
        }

        if n2 == -1 {
            return false
        }

        if a[n1] != b[n2] {
            return a[n1] < b[n2]
        }

        n1--
        n2--
    }
}

func smallestFromLeaf(root *TreeNode) string {
    var exploreNode func(*TreeNode, []int) []int
    exploreNode = func(node *TreeNode, path []int)[]int {
        if node == nil{
            return path
        }

        path = append(path, node.Val)
        if node.Left != nil && node.Right != nil {
            left_copy := append([]int{}, path...)
            right_copy := append([]int{}, path...)
            left_path := exploreNode(node.Left, left_copy)
            right_path := exploreNode(node.Right, right_copy)
            left_smaller := compare(left_path, right_path)
            if left_smaller {
                return left_path
            } else {
                return right_path
            }
        } else if node.Left != nil {
            return exploreNode(node.Left, path)
        } else if node.Right != nil {
            return exploreNode(node.Right, path)
        } else {
            return path
        }
    }

    arr := exploreNode(root, []int{})
    n := len(arr)
    var ans strings.Builder
    for i := n-1; i >= 0; i-- {
        ans.WriteRune(rune(arr[i]+97))
    }
    return ans.String()
}

