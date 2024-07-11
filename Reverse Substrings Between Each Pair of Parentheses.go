func reverseParentheses(s string) string {
    var accumulate func (i int, n int) ([]byte, int)
    accumulate = func (i int, n int) ([]byte, int) {
        arr := make([]byte, 0)
        for {
            if i >= n {
                return arr, i
            }

            if s[i] == ')' {
                slices.Reverse(arr)
                return arr, i+1
            }

            if s[i] == '(' {
                arr2, j := accumulate(i+1, n)
                arr = append(arr, arr2...)
                i = j
                continue
            }

            arr = append(arr, s[i])
            i++
        }
    }

    arr, _ := accumulate(0, len(s))
    var ans strings.Builder
    for _, r := range arr {
        ans.WriteByte(r)
    }
    return ans.String()
}
