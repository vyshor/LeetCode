func bagOfTokensScore(tokens []int, power int) int {
    n := len(tokens)
    if n == 0 {
        return 0
    }

    slices.Sort(tokens)
    var maxx, score int
    i := 0
    j := n-1
    for i < n && power >= tokens[i] && i <= j {
        for i < n && power >= tokens[i] && i <= j {
            power -= tokens[i]
            i += 1
            score += 1
        }

        maxx = max(maxx, score)
        if score > 0 && i <= j {
            power += tokens[j]
            j -= 1
            score -= 1
        }
    }
    return maxx
}
