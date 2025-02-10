func isDigit(b byte) bool {
    return b >= byte('0') && b <= byte('9')
}

func clearDigits(s string) string {
    stack := make([]int, 0)
    n := len(s)
    mask := make([]int, n)
    for i := 0; i < n; i++ {
        c := s[i]
        mask[i] = 1
        if isDigit(c) && len(stack) > 0 {
            mask[stack[len(stack)-1]] = 0
            stack = stack[:len(stack)-1]
            mask[i] = 0
        } else if !isDigit(c) {
            stack = append(stack, i)
        }
    }

    var ss strings.Builder
    for i := 0; i < n; i++ {
        if mask[i] == 1 {
            ss.WriteByte(s[i])
        }
    }
    return ss.String()
}