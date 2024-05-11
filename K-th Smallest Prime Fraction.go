type Fact struct {
    frac float64
    num int
    den int
}

type FactHeap []Fact

func (h FactHeap) Len() int           { return len(h) }
func (h FactHeap) Less(i, j int) bool { return h[i].frac < h[j].frac }
func (h FactHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *FactHeap) Push(x any) {
	*h = append(*h, x.(Fact))
}

func (h *FactHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
    n := len(arr)
    q := &FactHeap{}
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            heap.Push(q, Fact{frac: -float64(arr[i])/float64(arr[j]), num: arr[i], den: arr[j]})

            if q.Len() > k {
                heap.Pop(q)
            }
        }
    }
    fact := heap.Pop(q).(Fact)
    return []int{fact.num, fact.den}
}
