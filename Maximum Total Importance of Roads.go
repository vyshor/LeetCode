func maximumImportance(n int, roads [][]int) int64 {
    arr := make([]int64, n)
    for _, road := range roads {
        arr[road[0]]++
        arr[road[1]]++
    }

    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
    var summ int64
    n2 := int64(n)
    for n2 > 0 {
        summ += n2*arr[n2-1]
        n2--
    }
    return summ
}
