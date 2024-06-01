func abs(i int) int {
    if i < 0 {
        return -i
    }
    return i
}

func scoreOfString(s string) int {
    score := 0
    r := []rune(s)
    n := len(r)
    prev := r[0]
    for i := 1; i < n; i++ {
        current := r[i]
        score += abs(int(current-prev))
        prev = current
    }
    return score
}

