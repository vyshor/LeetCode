type Item struct {
    f float64
    i int
}
type FloatHeap []Item

func (h FloatHeap) Len() int           { return len(h) }
func (h FloatHeap) Less(i, j int) bool { return h[i].f > h[j].f }
func (h FloatHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *FloatHeap) Push(x any) {
	*h = append(*h, x.(Item))
}

func (h *FloatHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
    dp := make(map[int]map[int]float64)
    for i, edge := range edges {
        prob := succProb[i]
        u := edge[0]
        v := edge[1]
        if _, ok := dp[u]; !ok {
            dp[u] = make(map[int]float64)
        }
        if _, ok := dp[v]; !ok {
            dp[v] = make(map[int]float64)
        }
        dp[u][v] = prob
        dp[v][u] = prob
    }

    visited := make(map[int]interface{})
    h := &FloatHeap{{f:1.0, i:start_node}}
    for h.Len() > 0 {
        item := heap.Pop(h).(Item)
        prob := item.f
        node := item.i
        if node == end_node {
            return prob
        }

        if _, ok := visited[node]; ok {
            continue
        }

        visited[node] = nil
        if _, ok := dp[node]; !ok {
            continue
        }

        for other, cost := range dp[node] {
            if _, ok := visited[other]; !ok {
                heap.Push(h, Item{f: cost*prob, i:other})
            }
        }
    }
    return 0.
}
