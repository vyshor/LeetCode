type IntHeap []int64

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int64))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minOperations(nums []int, k int) int {
    arr := make(IntHeap, 0)
    for _, num := range nums {
        if num < k {
            arr = append(arr, int64(num))
        }
    }
    n := len(arr)
    h := &arr
    count := 0
	heap.Init(h)

    for n > 1 {
        minn := heap.Pop(h).(int64)
        minn2 := heap.Pop(h).(int64)
        x := (minn << 1) + minn2
        if x < int64(k) {
            heap.Push(h, x)
            n--
        } else {
            n -= 2
        }
        count++
    }
    return count + n
}
