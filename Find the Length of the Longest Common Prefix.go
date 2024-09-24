type Node struct {
    Route map[byte]*Node
    End bool
}

func NewNode() *Node {
    return &Node{
        Route: make(map[byte]*Node),
    }
}

func (n *Node) add(word string, idx int) {
    if len(word) == idx {
        n.End = true
        return
    }

    c := word[idx]
    if _, ok := n.Route[c]; !ok {
        n.Route[c] = NewNode()
    }
    n.Route[c].add(word, idx+1)
}

func (n *Node) find(word string, idx int) int {
    if len(word) == idx {
        return idx
    }

    c := word[idx]
    if _, ok := n.Route[c]; !ok {
        return idx
    }
    return n.Route[c].find(word, idx+1)
}

func longestCommonPrefix(arr1 []int, arr2 []int) int {
    trie := NewNode()
    for _, i := range arr1 {
        word := strconv.Itoa(i)
        trie.add(word, 0)
    }

    maxx := 0
    for _, i := range arr2 {
        word := strconv.Itoa(i)
        maxx = max(maxx, trie.find(word, 0))
    }
    return maxx
}
