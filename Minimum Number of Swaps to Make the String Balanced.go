func minSwaps(s string) int {
    n := 0
    count := 0
    for _, c := range s {
        if c == '[' {
            n++
        } else if n == 0 {
            count++
            n++
        } else {
            n--
        }
    }
    return count
}
