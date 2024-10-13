func minAddToMakeValid(s string) int {
    var count, n int
    for _, c := range s {
        if c == '(' {
            n++
        } else if n == 0 {
            count++
        } else {
            n--
        }
    }
    return count + n
}
