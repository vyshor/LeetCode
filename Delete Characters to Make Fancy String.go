func makeFancyString(s string) string {
    n := len(s)
    if n <= 2 {
        return s
    }

    a := s[0]
    b := s[1]
    var ss strings.Builder
    ss.WriteByte(a)
    ss.WriteByte(b)
    i := 2
    for i < n {
        c := s[i]
        i++
        if c != b || b != a {
            ss.WriteByte(c)
            a = b
            b = c
        }
    }
    return ss.String()
}
