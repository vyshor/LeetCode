func groupAnagrams(strs []string) [][]string {
    counter := make(map[string][]string)
    for _, word := range strs {
        arr := make([]int, 26)
        for _, c := range word {
            arr[c - 97]++
        }
        key := fmt.Sprint(arr)
        if _, ok := counter[key]; ok {
            counter[key] = append(counter[key], word)
        } else {
            counter[key] = []string{word}
        }
    }

    n := len(counter)
    ans := make([][]string, n)
    i := 0
    for _, words := range counter {
        ans[i] = words
        i++
    }
    return ans
}
