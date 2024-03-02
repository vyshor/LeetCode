func makeSmallestPalindrome(s string) string {
    n := len(s)
    c := make([]rune, n)
    for i, ch := range s {
        c[i] = ch
    }

    i := 0
    j := n-1
    for i < j {
        if c[i] != c[j] {
            r := min(c[i], c[j])
            c[i] = r
            c[j] = r
        }
        i++
        j--
    }

    var ans strings.Builder
    for _, ch := range c {
        ans.WriteRune(ch)
    }
    return ans.String()
}
