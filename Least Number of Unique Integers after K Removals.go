func findLeastNumOfUniqueInts(arr []int, k int) int {
    counter := make(map[int]int)
    for _, num := range arr {
        if _, ok := counter[num]; ok {
            counter[num] += 1
        } else {
            counter[num] = 1
        }
    }

    n := len(counter)
    counts := make([]int, n)
    j := 0
    for _, count := range counter {
        counts[j] = count
        j++
    }
    slices.Sort(counts)

    for i, count := range counts {
        if k < count {
            return n-i
        } else {
            k -= count
        }
    }
    return 0
}
