func countPalindromicSubsequence(s string) int {
    last_seen := make(map[byte]int)
    opened := make(map[byte]interface{})
    ans := make(map[int]interface{})

    n := len(s)
    for i := 0; i < n; i++ {
        last_seen[s[i]] = i
    }

    for i := 0; i < n; i++ {
        c := s[i]
        if i < last_seen[c] {
            for cx := range opened {
                h := (1 << (cx - 96 + 26)) | (1 << (c - 96))
                ans[h] = nil
            }

            opened[c] = nil
        } else {
            delete(opened, c)

            for cx := range opened {
                h := (1 << (cx - 96 + 26)) | (1 << (c - 96))
                ans[h] = nil
            }
        }
    }
    return len(ans)
}