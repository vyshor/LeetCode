/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func modifiedList(nums []int, head *ListNode) *ListNode {
    seen := make(map[int]interface{})
    for _, num := range nums {
        seen[num] = nil
    }

    dummy := ListNode{Next:head}
    prev, ptr := &dummy, head
    for ptr != nil {
        if _, ok := seen[ptr.Val]; ok {
            prev.Next = ptr.Next
            ptr = ptr.Next
        } else {
            prev = ptr
            ptr = ptr.Next
        }
    }
    return dummy.Next
}
