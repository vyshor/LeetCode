func maximumGain(s string, x int, y int) int {
    score := 0

    find_ab := func(s []byte, a, b byte, delta int) []byte {
        n := len(s)
        stack := make([]byte, 0)
        for i := 0; i < n; i++ {
            if s[i] == b && len(stack) > 0 && stack[len(stack)-1] == a {
                score += delta
                stack = stack[:len(stack)-1]
            } else {
                stack = append(stack, s[i])
            }
        }
        return stack
    }

    stack := []byte(s)
    if x > y {
        find_ab(find_ab(stack, 'a', 'b', x), 'b', 'a', y)
    } else {
        find_ab(find_ab(stack, 'b', 'a', y), 'a', 'b', x)
    }
    return score
}
