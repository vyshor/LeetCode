/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func splitListToParts(head *ListNode, k int) []*ListNode {
    n := 0
    ptr := head
    for ptr != nil {
        n++
        ptr = ptr.Next
    }

    m := n / k
    k2 := n % k
    ptr = head
    arr := make([]*ListNode, 0)
    for ptr != nil {
        arr = append(arr, ptr)
        i := 0
        addon := -1
        if k2 > 0 {
            addon++
        }
        for i < (m + addon) && ptr != nil {
            ptr = ptr.Next
            i++
        }
        k2--
        nxt := ptr.Next
        ptr.Next = nil
        ptr = nxt
    }

    for len(arr) < k {
        arr = append(arr, nil)
    }
    return arr
}
