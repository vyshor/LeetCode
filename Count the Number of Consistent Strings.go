func countConsistentStrings(allowed string, words []string) int {
    dp := make(map[rune]interface{})
    for _, c := range allowed {
        dp[c] = nil
    }

    count := 0
    for _, word := range words {
        can := true
        for _, c := range word {
            if _, ok := dp[c]; !ok {
                can = false
                break
            }
        }
        if can {
            count += 1
        }
    }
    return count
}
