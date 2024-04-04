func maxDepth(s string) int {
    var open_count, maxx int
    for _, c := range s {
        if c == '(' {
            open_count++
            maxx = max(maxx, open_count)
        } else if c == ')' {
            open_count--
        }
    }
    return maxx
}
