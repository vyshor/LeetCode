func maxUniqueSplit(s string) int {
    n := len(s)
    seen := make(map[string]interface{})
    word := make([]byte, 0)
    count := 0
    maxx := 0
    var recur func(i int)
    recur = func(i int) {
        if i == n {
            if _, ok := seen[string(word)]; !ok {
                if count+1 > maxx {
                    maxx = count+1
                }
            }
            return
        }

        word = append(word, s[i])
        recur(i+1)
        word = word[:len(word)-1]

        formed := string(word)
        if len(word) == 0 {
            return
        }

        if _, ok := seen[formed]; !ok {
            old_word := word
            seen[formed] = nil
            count++
            word = []byte{s[i]}

            recur(i+1)

            word = old_word
            delete(seen, formed)
            count--
        }
    }
    recur(0)
    return maxx
}
