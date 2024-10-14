// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
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

func maxKelements(nums []int, k int) int64 {
    q := IntHeap(nums)
    heap.Init(&q)
    score := int64(0)
    for k > 0 {
        val := heap.Pop(&q).(int)
        score += int64(val)
        heap.Push(&q, int(math.Ceil(float64(val)/3.)))
        k--
    }
    return score
}
