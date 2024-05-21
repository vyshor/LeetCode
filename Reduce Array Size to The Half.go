func minSetSize(arr []int) int {
    n := len(arr)
    mid := n / 2 + (n % 2)
    counter := make(map[int]int)
    for _, num := range arr {
        if _, ok := counter[num]; !ok {
            counter[num] = 1
        } else {
            counter[num]++
        }
    }

    vals := make([]int, 0)
    for _, num := range counter {
        vals = append(vals, -num)
    }
    sort.Ints(vals)
    for i, val := range vals {
        n += val
        if n <= mid {
            return i+1
        }
    }
    return 0
}
