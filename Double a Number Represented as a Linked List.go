/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
    dummyHead := &ListNode{Next:head}
    prev := dummyHead
    ptr := head
    for ptr != nil {
        ptr.Val *= 2
        prev.Val += ptr.Val / 10
        ptr.Val %= 10
        prev = ptr
        ptr = ptr.Next
    }

    if dummyHead.Val != 0 {
        return dummyHead
    }
    return dummyHead.Next
}
