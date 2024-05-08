func findRelativeRanks(score []int) []string {
    arr := append(score[:0:0], score...)
    sort.Ints(arr)
    n := len(score)
    scores := make(map[int]string)
    names := []string{"Gold Medal", "Silver Medal", "Bronze Medal"}
    for i := 0; i < n; i++ {
        j := n-1-i
        if i < 3 {
            scores[arr[j]] = names[i]
        } else {
            scores[arr[j]] = strconv.Itoa(i+1)
        }
    }

    ans := make([]string, n)
    for i := 0 ; i<n; i++ {
        ans[i] = scores[score[i]]
    }
    return ans
}
