type cls struct {
    inc float64
    p int
    t int
}

type CHeap []cls

func (h CHeap) Len() int           { return len(h) }
func (h CHeap) Less(i, j int) bool { return h[i].inc < h[j].inc }
func (h CHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *CHeap) Push(x any) {
	*h = append(*h, x.(cls))
}
func (h *CHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
    var summ float64
    count := len(classes)
    h := CHeap{}
    i := extraStudents
    for _, c := range classes {
        pp := c[0]
        tt := c[1]
        if pp == tt {
            summ += float64(1)
            continue
        }

        p := float64(pp)
        t := float64(tt)
        h = append(h, cls{p/t- (p+1)/(t+1), pp, tt})
    }

    if len(h) == 0 {return float64(1)}

    heap.Init(&h)
    for i > 0 {
        cur := heap.Pop(&h).(cls)
        cur.p++
        cur.t++
        p := float64(cur.p)
        t := float64(cur.t)
        cur.inc = p/t- (p+1)/(t+1)
        heap.Push(&h, cur)
        i--
    }

    for _, cur := range h {
        p := float64(cur.p)
        t := float64(cur.t)
        summ += p/t
    }
    return summ / float64(count)
}