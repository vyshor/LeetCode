func heightChecker(heights []int) int {
    new_heights := append([]int{}, heights...)
    sort.Ints(new_heights)
    count := 0
    for i := 0; i < len(heights); i++ {
        if (heights[i] != new_heights[i]) {
            count++
        }
    }
    return count
}
