/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
    b += 2 - a

    pt := list1
    for a > 1 {
        pt = pt.Next
        a--
    }

    pt2 := pt
    for b > 0 {
        pt2 = pt2.Next
        b--
    }

    pt.Next = list2
    for pt.Next != nil {
        pt = pt.Next
    }

    pt.Next = pt2
    return list1
}
