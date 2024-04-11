func removeKdigits(num string, k int) string {
    n := len(num)
    if k == n {
        return "0"
    }

    stack := make([]rune, 0)
    for _, j := range num {
        for len(stack) > 0 && stack[len(stack)-1] > j && k > 0 {
            stack = stack[:len(stack)-1]
            k--
        }
        stack = append(stack, j)
    }

    stack = stack[:len(stack)-k]

    ans := string(stack)
    ans = strings.TrimLeft(ans, "0")
    if ans == "" {
        return "0"
    }
    return ans

}
