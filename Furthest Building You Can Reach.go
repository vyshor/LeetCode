import "container/heap"

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

type Diff struct {
    i int
    diff int
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
    diffs := make([]Diff, 0)
    diffs = append(diffs, Diff{i: 0, diff: 0})
    h := heights[0]
    n := len(heights)
    for i := 1; i < n; i++ {
        if heights[i] > h {
            diffs = append(diffs, Diff{i:i, diff: heights[i]-h})
        } else {
            diffs[len(diffs)-1].i = i
        }
        h = heights[i]
    }

    m := len(diffs)
    if ladders >= m-1 {
        return n-1
    }

    q := &IntHeap{}
	heap.Init(q)

    for i := 1; i <= ladders; i++ {
        heap.Push(q, diffs[i].diff)
    }

    pos := diffs[ladders].i
    i := ladders+1
    for i < m && bricks > 0 {
        heap.Push(q, diffs[i].diff)
        bricks -= heap.Pop(q).(int)
        if bricks < 0 {
            return pos
        }
        pos = diffs[i].i
        i++
    }
    return pos
}
