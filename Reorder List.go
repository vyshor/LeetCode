/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    if head.Next == nil {
        return
    }

    slow := head
    fast := head.Next
    for fast.Next != nil {
        fast = fast.Next
        slow = slow.Next

        if fast.Next == nil {
            break
        }
        fast = fast.Next
    }

    pt := slow.Next
    slow.Next = nil
    n := pt.Next
    pt.Next = nil

    for n != nil {
        n2 := n.Next
        n.Next = pt
        pt = n
        n = n2
    }

    pt1 := head
    pt2 := pt
    for pt1 != nil && pt2 != nil {
        pt3 := pt2.Next
        pt2.Next = pt1.Next
        pt1.Next = pt2
        pt1 = pt1.Next.Next
        pt2 = pt3
    }

}

