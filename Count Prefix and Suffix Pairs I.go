func compare(wordA, wordB string) int {
    if len(wordA) > len(wordB) {
        return 0
    }
    i := 0
    j := len(wordB) - len(wordA)
    for i < len(wordA) {
        if wordA[i] != wordB[i] || wordA[i] != wordB[j] {
            return 0
        }
        i++
        j++
    }
    return 1
}

func countPrefixSuffixPairs(words []string) int {
    n := len(words)
    count := 0
    for i := 0; i < n; i++ {
        for j := 0; j < i; j++ {
            count += compare(words[j], words[i])
        }
    }
    return count
}

