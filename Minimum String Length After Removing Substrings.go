func minLength(s string) int {
    stack := make([]byte, 0)
    for i := range s {
        if s[i] == 'D' && len(stack) > 0 && stack[len(stack)-1] == 'C' {
            stack = stack[:len(stack)-1]
        } else if s[i] == 'B' && len(stack) > 0 && stack[len(stack)-1] == 'A' {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, s[i])
        }
    }
    return len(stack)
}
