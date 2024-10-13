type Tuple struct {
	V int
    I int
    J int
}

// An TupleHeap is a min-heap of ints.
type TupleHeap []Tuple

func (h TupleHeap) Len() int { return len(h) }
func (h TupleHeap) Less(i, j int) bool {
    return h[i].V < h[j].V
}
func (h TupleHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *TupleHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(Tuple))
}

func (h *TupleHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func smallestRange(nums [][]int) []int {
    q := TupleHeap{}
    maxx := nums[0][0]
    for i, arr := range nums {
        maxx = max(maxx, arr[0])
        q = append(q, Tuple{V: arr[0], I:i, J: 0})
    }

    heap.Init(&q)
    minn := maxx - q[0].V
    ans := []int{q[0].V, maxx}

    for {
        if maxx - q[0].V < minn {
            minn = maxx - q[0].V
            ans = []int{q[0].V, maxx}
        }

        v := heap.Pop(&q).(Tuple)
        if v.J+1 == len(nums[v.I]) {
            return ans
        }

        heap.Push(&q, Tuple{V:nums[v.I][v.J+1], I: v.I, J:v.J+1})
        maxx = max(maxx, nums[v.I][v.J+1])
    }
}
