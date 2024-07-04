/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
    ptr := head.Next
    new_ptr := head
    summ := 0
    for ptr != nil {
        for ptr.Val != 0 {
            summ += ptr.Val
            ptr = ptr.Next
        }

        new_ptr.Val = summ
        summ = 0
        ptr = ptr.Next
        if ptr == nil {
            new_ptr.Next = nil
        } else {
            new_ptr = new_ptr.Next
        }
    }
    new_ptr.Next = nil
    return head
}
