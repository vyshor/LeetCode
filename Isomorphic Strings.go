func isIsomorphic(s string, t string) bool {
    dp := make(map[rune]rune)
    seen := make(map[rune]interface{})

    if len(s) != len(t) {
        return false
    }

    t2 := []rune(t)

    for i, c := range s {
        if r, ok := dp[c]; ok && r != t2[i] {
            return false
        }

        _, ok := seen[t2[i]]
        if _, ok2 := dp[c]; ok && !ok2 {
            return false
        }

        dp[c] = t2[i]
        seen[t2[i]] = nil
    }
    return true
}
