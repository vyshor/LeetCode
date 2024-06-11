func relativeSortArray(arr1 []int, arr2 []int) []int {
    counter := make(map[int]int)
    for _, num := range arr1 {
        counter[num]++
    }

    ans := make([]int, 0)
    for _, num := range arr2 {
        count := counter[num]
        for i := 0; i < count; i++ {
            ans = append(ans, num)
        }
        delete(counter, num)
    }

    remaining := make([]int, 0)
    for num, count := range counter {
        for i := 0; i < count; i++ {
            remaining = append(remaining, num)
        }
    }
    sort.Ints(remaining)

    return append(ans, remaining...)
}
