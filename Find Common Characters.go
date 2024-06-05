func count(s string) []int {
    counter := make([]int, 26)
    for _, c := range s {
        counter[c-97]++
    }
    return counter
}

func commonChars(words []string) []string {
    counter := count(words[0])
    n := len(words)
    for i := 1; i < n; i++ {
        counter2 := count(words[i])
        for j := 0; j < 26; j++ {
        counter[j] = min(counter[j], counter2[j])
        }
    }

    ans := make([]string, 0)
    for i, c := range counter {
        for j := 0; j < c; j++ {
            ans = append(ans, string(i+97))
        }
    }
    return ans
}
