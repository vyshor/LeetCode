/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    pt := head
    arr := make([]int, 0)
    for pt != nil {
        arr = append(arr, pt.Val)
        pt = pt.Next
    }

    i := 0
    j := len(arr)-1
    for i < j {
        if arr[i] != arr[j] {
            return false
        }
        i++
        j--
    }
    return true
}
