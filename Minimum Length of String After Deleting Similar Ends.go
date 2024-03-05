func minimumLength(s string) int {
    i := 0
    j := len(s) - 1

    for s[i] == s[j] && i != j {
        c := s[i]
        i += 1
        for i <= j && s[i] == c {
            i++
        }

        j--
        for j >= i && s[j] == c {
            j -= 1
        }

        if j < i {
            return 0
        }
    }
    return j-i+1
}
