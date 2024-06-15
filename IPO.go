// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Pair struct {
    capital int
    profit int
}

type PairHeap []Pair

func (h PairHeap) Len() int           { return len(h) }
func (h PairHeap) Less(i, j int) bool { return h[i].capital < h[j].capital }
func (h PairHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *PairHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(Pair))
}

func (h *PairHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}


func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
    n := len(profits)
    q := IntHeap{}
    q2 := PairHeap{}

    for i := 0; i < n; i++ {
        if w >= capital[i] {
            q = append(q, -profits[i])
        } else {
            q2 = append(q2, Pair{capital: capital[i], profit: profits[i]})
        }
    }

    heap.Init(&q)
    heap.Init(&q2)

    if len(q) == 0 {
        return w
    }

    w -= heap.Pop(&q).(int)
    k--

    for k > 0 {
        for len(q2) > 0 && q2[0].capital <= w {
            pair := heap.Pop(&q2).(Pair)
            heap.Push(&q, -pair.profit)
        }

        if len(q) == 0 {
            break
        }

        w -= heap.Pop(&q).(int)
        k--
    }
    return w
}
