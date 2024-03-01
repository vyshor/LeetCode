func maximumOddBinaryNumber(s string) string {
    n := len(s)
    count := 0
    for _, c := range(s) {
        if c == '1' {
            count++
        }
    }

    var ans strings.Builder
    n--
    for n > 0 {
        if count > 1 {
            ans.WriteRune('1')
            count--
        } else {
            ans.WriteRune('0')
        }
        n--
    }
    ans.WriteRune('1')
    return ans.String()
}
