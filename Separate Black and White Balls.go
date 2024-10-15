func minimumSteps(s string) int64 {
    count := int64(0);
    n := len(s)
    var left, right int
    for right < n {
        if s[right] == '0' {
            count += int64(right-left)
            left++
        }
        right++
    }
    return count
}
