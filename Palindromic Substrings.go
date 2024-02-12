func countSubstrings(s string) int {
    dp := make(map[int]bool)
    checkMatch := func (i, j int) bool {
        key := i << 16 | j
        if val, ok := dp[key]; ok {
            return val
        } else {
            dp[key] = s[i] == s[j]
            return dp[key]
        }
    }

    n := len(s)
    count := 0
    var checkPalindrome func(i, j int);
    checkPalindrome = func(i, j int) {
        if i >= 0 && i < n && j >= 0 && j < n && checkMatch(i, j) {
            count += 1
            checkPalindrome(i-1, j+1)
        }
    }

    for i := 0; i < n; i++ {
        checkPalindrome(i, i)
        checkPalindrome(i, i+1)
    }

    return count
}
