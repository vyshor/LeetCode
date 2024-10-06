func areSentencesSimilar(sentence1 string, sentence2 string) bool {
    splits1 := strings.Split(sentence1, " ")
    splits2 := strings.Split(sentence2, " ")
    if len(splits1) > len(splits2) {
        splits1, splits2 = splits2, splits1
    }

    n1, n2 := len(splits1), len(splits2)
    if n1 == 1 {
        return splits2[0] == splits1[0] || splits2[n2-1] == splits1[0]
    }

    l1, r1 := 0, n1 - 1
    r2 := n2 - 1
    for l1 < n1 && splits1[l1] == splits2[l1] {
        l1++
    }

    for r1 >= l1 && splits1[r1] == splits2[r2] {
        r1--
        r2--
    }

    return r1 < l1
}
