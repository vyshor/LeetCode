type Person struct {
    n string
    h int
}

func sortPeople(names []string, heights []int) []string {
    n := len(names)
    arr := make([]Person, n)
    for i := 0; i < n; i++ {
        arr[i].n = names[i]
        arr[i].h = heights[i]
    }
    sort.Slice(arr, func (a, b int) bool {
        return arr[a].h > arr[b].h
    })
    arr2 := make([]string, n)
    for i := 0; i < n; i++ {
        arr2[i] = arr[i].n
    }
    return arr2
}
