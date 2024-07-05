/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
    minn, maxx := 1 << 17, 0
    first_idx, prev_idx := -1, -1
    i := 1
    ptr, prev := head.Next, head
    for ptr.Next != nil {
        critical := (prev.Val < ptr.Val && ptr.Val > ptr.Next.Val) || (prev.Val > ptr.Val && ptr.Val < ptr.Next.Val)
        if critical {
            if first_idx == -1 {
                first_idx = i
            }

            if prev_idx != -1 {
                minn = min(minn, i-prev_idx)
                maxx = max(maxx, i-first_idx)
            }
            prev_idx = i
        }

        prev, ptr = ptr, ptr.Next
        i++
    }

    if prev_idx == first_idx  {
        return []int{-1, -1}
    }
    return []int{minn, maxx}
}
