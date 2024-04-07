func checkValidString(s string) bool {
    var lo, hi int
    for _, c := range s {
        if c == '(' {
            lo++
            hi++
        } else if c == ')' {
            lo = max(lo-1, 0)
            hi--
            if hi < 0 {
                return false
            }
        } else {
            lo = max(lo-1, 0)
            hi++
        }
    }
    return lo == 0
}
