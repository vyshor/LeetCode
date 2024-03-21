/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    pt1 := head
    pt2 := head.Next
    pt1.Next = nil

    for pt2 != nil {
        pt3 := pt2.Next
        pt2.Next = pt1
        pt1 = pt2
        pt2 = pt3
    }
    return pt1
}
