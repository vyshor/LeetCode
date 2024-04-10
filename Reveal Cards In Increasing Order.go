type Node struct {
    val int
    next *Node
    prev *Node
}

var head, tail *Node

func Pop() *Node {
    var node *Node
    if head == tail {
        node = tail
        tail = nil
        head = nil
    } else {
        tail.prev.next = nil
        node = tail
        tail = tail.prev
    }

    node.next = nil
    node.prev = nil
    return node
}

func Enque(n *Node) {
    if head == nil && tail == nil {
        head = n
        tail = n
    } else {
        head.prev = n
        n.next = head
        head = n
    }
}

func deckRevealedIncreasing(deck []int) []int {
    head = nil
    tail = nil

    n := len(deck)
    sort.Ints(deck)
    i := n-2

    node := Node{val: deck[n-1], next: nil, prev: nil}
    Enque(&node)

    for i >= 0 {
        orphan := Pop()
        Enque(orphan)
        new_node := Node{val: deck[i], next:nil, prev:nil}
        Enque(&new_node)
        i--
    }

    ans := make([]int, n)
    i = 0
    pt := head
    for (i < n) {
        ans[i] = pt.val
        pt = pt.next
        i++
    }
    return ans
}

