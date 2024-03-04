/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummyHead := &ListNode{
        Val: 0,
        Next: head,
    }
    m := 1
    pt := head
    for pt.Next != nil {
        pt = pt.Next
        m += 1
    }

    m -= n
    pt = dummyHead
    for m > 0 {
        pt = pt.Next
        m -= 1
    }
    pt.Next = pt.Next.Next

    return dummyHead.Next
}

