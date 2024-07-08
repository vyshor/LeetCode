type Node struct {
    Next *Node
    Val int
}

func findTheWinner(n int, k int) int {
    head := &Node{Val:1}
    ptr := head
    for i := 2; i < n+1; i++ {
        ptr.Next = &Node{Val:i}
        ptr = ptr.Next
    }
    ptr.Next = head

    prev := ptr
    ptr = head

    count := k-1
    for prev != ptr {
        if count == 0 {
            prev.Next = ptr.Next
            ptr = ptr.Next
            count = k-1
        } else {
            prev, ptr = ptr, ptr.Next
            count--
        }
    }
    return ptr.Val
}
