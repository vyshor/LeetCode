/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func countPairs(root *TreeNode, distance int) int {
    count := 0
    var explore func(*TreeNode) map[int]int
    explore = func(node *TreeNode) map[int]int {
        if node == nil {
            return map[int]int{}
        }

        if node.Left == nil && node.Right == nil {
            return map[int]int{0:1}
        }

        counter := make(map[int]int)
        left_counter := explore(node.Left)
        right_counter := explore(node.Right)
        for k, v := range left_counter {
            for k2, v2 := range right_counter {
                if k+k2+2 <= distance {
                    count += v * v2
                }
            }

            if k+1 < distance {
                counter[k+1] += v
            }
        }

        for k, v := range right_counter {
            if k+1 < distance {
                counter[k+1] += v
            }
        }

        return counter
    }
    explore(root)
    return count
}
