func isCircularSentence(sentence string) bool {
    n := len(sentence)
    for i := 0; i < n; i++ {
        if sentence[i] == ' ' {
            if sentence[i-1] != sentence[i+1] {
                return false
            }
        }
    }

    return sentence[0] == sentence[n-1]
}
