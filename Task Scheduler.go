
type Task struct {
    t byte
    Count int
}

type IntHeap []Task

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].Count > h[j].Count }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    // Push and Pop use pointer receivers because they modify the slice's length,
    // not just its contents.
    *h = append(*h, x.(Task))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func leastInterval(tasks []byte, n int) int {
    maxx := len(tasks)
    counter := make(map[byte]int)
    for _, task := range tasks {
        if _, ok := counter[task]; !ok {
            counter[task] = 1
        } else {
            counter[task]++
        }
    }

    var h IntHeap
    heap.Init(&h)
    for k, count := range counter {
        heap.Push(&h, Task{
            t: k,
            Count: count,
        })
    }

    task := heap.Pop(&h).(Task)
    first_count := task.Count
    first_max := n*(first_count-1)+first_count
    maxx = max(maxx, first_max)
    for len(h) > 0 && h[0].Count == first_count {
        heap.Pop(&h)
        first_max++
        maxx = max(maxx, first_max)
    }
    return maxx
}
