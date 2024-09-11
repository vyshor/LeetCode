/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func gcd(a, b int) int {
    if b == 0 {
        return a
    }
    return gcd(b, a % b)
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    cur := head
    var prev *ListNode
    pval, cval := 0, head.Val
    for cur.Next != nil {
        prev, cur = cur, cur.Next
        pval, cval = cval, cur.Val
        prev.Next = &ListNode{Val:gcd(pval, cval), Next:cur}
    }
    return head
}
