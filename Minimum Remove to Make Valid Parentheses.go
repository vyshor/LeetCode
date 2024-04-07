func minRemoveToMakeValid(s string) string {
    stack := make([]int, 0)
    removed := make(map[int]interface{})
    for i, c := range s {
        if c == ')' {
            if len(stack) == 0 {
                removed[i] = nil
            } else {
                stack = stack[:len(stack)-1]
            }
        } else if c == '(' {
            stack = append(stack, i)
        }
    }

    for _, i := range stack {
        removed[i] = nil
    }

    var new_str strings.Builder
    for i, c := range s {
        if _, ok := removed[i]; !ok {
            new_str.WriteRune(c)
        }
    }
    return new_str.String()
}
