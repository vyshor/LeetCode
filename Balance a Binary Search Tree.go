/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func read(node* TreeNode, arr *[]int) {
    if node != nil {
        read(node.Left, arr)
        *arr = append(*arr, node.Val)
        read(node.Right, arr)
    }
}

func balance(left int, right int, arr *[]int) *TreeNode {
    if left == right {
        return &TreeNode{Val: (*arr)[left]}
    }

    if left > right {
        return nil
    }

    mid := (left+right)/2
    node := TreeNode{Val: (*arr)[mid]}
    node.Left = balance(left, mid-1, arr)
    node.Right = balance(mid+1, right, arr)
    return &node
}

func balanceBST(root *TreeNode) *TreeNode {
    arr := make([]int, 0)
    read(root, &arr)
    return balance(0, len(arr)-1, &arr)
}
