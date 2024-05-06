/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNodes(head *ListNode) *ListNode {
    stack := make([]*ListNode, 0)
    ptr := head

    for ptr != nil {
        for len(stack) > 0 && stack[len(stack)-1].Val < ptr.Val {
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, ptr)
        ptr = ptr.Next
    }

    for i := 0; i < len(stack)-1; i++ {
        stack[i].Next = stack[i+1]
    }
    return stack[0]
}
