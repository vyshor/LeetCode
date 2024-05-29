func numSteps(s string) int {
    n := len(s)
    r := []rune(s)
    var carry_over, steps int
    i := n-1
    for i > 0 {
        if (r[i] == '1' && carry_over == 0) || (r[i] == '0' && carry_over == 1) {
            steps += 2
            carry_over = 1
        } else {
            steps += 1
            if s[i] == '1' {
                carry_over = 1
            } else {
                carry_over = 0
            }
        }
        i--
    }
    return steps + carry_over
}
