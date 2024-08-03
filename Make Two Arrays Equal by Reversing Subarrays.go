func canBeEqual(target []int, arr []int) bool {
    counter := make(map[int]int)
    for _, num := range arr {
        counter[num]++
    }
    for _, num := range target {
        counter[num]--
        if counter[num] < 0 {
            return false
        }
    }
    return true
}
