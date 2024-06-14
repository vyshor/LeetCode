func countSubstrings(s string, c byte) int64 {
    var count int64
    n := len(s)
    for i := 0; i < n; i++ {
        if s[i] == c {
            count++
        }
    }
    return count * (count+1) /2
}

