type CountPair struct{
    r rune
    c int
}

func frequencySort(s string) string {
    counter := make(map[rune]int)
    for _, c := range s {
        if _, ok := counter[c]; ok {
            counter[c]++
        } else {
            counter[c] = 1
        }
    }

    arr := make([]CountPair, 0)
    for c, count := range counter {
        arr = append(arr, CountPair{c, count})
    }

    sort.Slice(arr, func(i, j int) bool {
	    return arr[i].c > arr[j].c
    })

    var ans strings.Builder
    for _, pair := range arr {
        _, _ = ans.WriteString(strings.Repeat(string(pair.r), pair.c))
    }

    return ans.String()
}
