type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Worker struct {
    rate float64
    quality int
}

func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
    n := len(quality)
    ratio := make([]Worker, 0)
    for i := 0; i < n; i++ {
        ratio = append(ratio, Worker{rate: float64(wage[i])/float64(quality[i]), quality: quality[i]})
    }
    sort.Slice(ratio, func (i, j int) bool{
        return ratio[i].rate < ratio[j].rate
    })

    rate := ratio[k-1].rate
    q := &IntHeap{}
    total := 0;
    for i := 0; i < k; i++ {
        heap.Push(q, -ratio[i].quality)
        total += ratio[i].quality
    }
    minn := rate*float64(total)
    for i := k; i < n; i++ {
        rate = ratio[i].rate
        heap.Push(q, -ratio[i].quality)
        total += ratio[i].quality + heap.Pop(q).(int)
        minn = min(minn, rate*float64(total))
    }
    return minn
}
