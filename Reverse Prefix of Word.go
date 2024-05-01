func reversePrefix(word string, ch byte) string {
    i := -1
    chr := rune(ch)
    for j, c := range word {
        if c == chr {
            i = j
            break
        }
    }

    if i == -1 {
        return word
    }

    var str strings.Builder
    str.Reset()
    for j := i; j >= 0; j-- {
        str.WriteByte(word[j])
    }
    str.WriteString(word[i+1:])
    return str.String()
}
