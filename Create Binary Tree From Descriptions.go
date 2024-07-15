/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func createBinaryTree(descriptions [][]int) *TreeNode {
    dp := make(map[int]*TreeNode)
    dp_incoming := make(map[int]int)
    for _, desc := range descriptions {
        p, c, l := desc[0], desc[1], desc[2]

        dp_incoming[c] += 1
        dp_incoming[p] += 0

        if dp[p] == nil {
            dp[p] = &TreeNode{Val: p}
        }

        if dp[c] == nil {
            dp[c] = &TreeNode{Val: c}
        }

        if l == 1 {
            dp[p].Left = dp[c]
        } else {
            dp[p].Right = dp[c]
        }
    }

    for k, v := range dp_incoming {
        if v == 0 {
            return dp[k]
        }
    }
    return nil
}
