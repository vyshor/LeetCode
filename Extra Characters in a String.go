func minExtraChar(s string, dictionary []string) int {
    ptrs := make(map[string][]int)
    for _, word := range dictionary {
        ptrs[word] = []int{0}
    }
    n := len(s)
    dp := make([]int, n+1)
    for i := 1; i <= n; i++ {
        dp[i] = dp[i-1]+1
        c := s[i-1]
        for word, all_pos := range ptrs {
            new_pos := []int{0}
            for _, pos := range all_pos {
                if word[pos] == c {
                    pos++
                    if pos == len(word) {
                        dp[i] = min(dp[i], dp[i-len(word)])
                    } else {
                        new_pos = append(new_pos, pos)
                    }
                }
            }
            ptrs[word] = new_pos
        }
    }
    return dp[n]
}
