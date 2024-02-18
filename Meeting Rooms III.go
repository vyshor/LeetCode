import (
	"container/heap"
    "container/list"
)

type MeetingHeap [][]int

func (h MeetingHeap) Len() int           { return len(h) }
func (h MeetingHeap) Less(i, j int) bool {
    if h[i][0] == h[j][0] {
        return h[i][1] < h[j][1]
    } else {
        return h[i][0] < h[j][0]
    }
}
func (h MeetingHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MeetingHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([]int))
}

func (h *MeetingHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}


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

func mostBooked(n int, meetings [][]int) int {
    const negative_shift = -100
    uses := make([]int, n)
    arr := make([]int, n)
    arr2 := IntHeap(arr)
    available := &arr2
    for i := 0; i < n; i++ {
        arr[i] = i
    }
    heap.Init(available)

    q := list.New()
    m2 := MeetingHeap(meetings)
    m := &m2
    heap.Init(m)
    for len(m2) > 0 {
        meeting := heap.Pop(m).([]int)
        if meeting[1] > 0 {
            q.PushBack(meeting)
        } else {
            heap.Push(available, meeting[1]-negative_shift)
        }

        for len(arr2) > 0 && q.Len() > 0 {
            waiting := q.Remove(q.Front()).([]int)
            duration := waiting[1] - waiting[0]
            room := heap.Pop(available).(int)
            uses[room] += 1
            heap.Push(m, []int{meeting[0]+duration, negative_shift+room})
        }
    }

    maxx_count := uses[0]
    j := 0
    for i, use := range uses {
        if use > maxx_count {
            j = i
            maxx_count = use
        }
    }

    return j
}
