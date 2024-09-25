type Node struct {
    Route map[byte]*Node
    Score int
}

func NewNode() *Node {
    return &Node{
        Route: make(map[byte]*Node),
    }
}

func (n *Node) add(word string, idx int) {
    if len(word) == idx {
        return
    }

    c := word[idx]
    if _, ok := n.Route[c]; !ok {
        n.Route[c] = NewNode()
    }
    n.Route[c].Score++
    n.Route[c].add(word, idx+1)
}

func (n *Node) find(word string, idx int) int {
    if len(word) == idx {
        return n.Score
    }

    c := word[idx]
    if _, ok := n.Route[c]; !ok {
        return n.Score
    }
    return n.Score + n.Route[c].find(word, idx+1)
}

func sumPrefixScores(words []string) []int {
    trie := NewNode()
    for _, word := range words {
        trie.add(word, 0)
    }

    arr := make([]int, 0)
    for _, word := range words {
        arr = append(arr, trie.find(word, 0))
    }
    return arr
}

