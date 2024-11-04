func compressedString(word string) string {
    var ss strings.Builder
    prev := rune(word[0])
    count := 0
    for _, c := range word {
        if prev == c {
            count++
            if count == 9 {
                ss.WriteString(strconv.Itoa(count))
                ss.WriteRune(prev)
                count = 0
            }
        } else {
            if count > 0 {
                ss.WriteString(strconv.Itoa(count))
                ss.WriteRune(prev)
            }
            prev = c
            count = 1
        }
    }

    if count > 0 {
        ss.WriteString(strconv.Itoa(count))
        ss.WriteRune(prev)
    }
    return ss.String()
}
