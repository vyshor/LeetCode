func kthDistinct(arr []string, k int) string {
    counter := make(map[string]int)
    for _, s := range arr {
        counter[s]++
    }

    for _, s := range arr {
        if counter[s] == 1 {
            k--
            if k == 0 {
                return s
            }
        }
    }
    return ""
}