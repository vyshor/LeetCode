/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }

    slow := head
    fast := head.Next
    for slow != fast {
        slow = slow.Next
        fast = fast.Next

        if fast == nil {
            return false
        }

        fast = fast.Next
        if fast == nil {
            return false
        }
    }
    return true
}
