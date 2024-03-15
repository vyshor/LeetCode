func customSortString(order string, s string) string {
    counter := make(map[rune]int)
    for _, c := range s {
        if _, ok := counter[c]; !ok {
            counter[c] = 1
        } else {
            counter[c]++
        }
    }

    var ans strings.Builder
    for _, c := range order {
        if _, ok := counter[c]; ok {
            for i := 0; i < counter[c]; i++ {
                ans.WriteRune(c)
            }
            delete(counter, c)
        }
    }

    for c, count := range counter {
        for i := 0; i < count; i++ {
            ans.WriteRune(c)
        }
    }
    return ans.String()
}
