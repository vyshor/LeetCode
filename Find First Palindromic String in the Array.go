func firstPalindrome(words []string) string {
    for _, word := range words {
        n := len(word)
        i := 0
        j := n-1
        palindrome := true

        for i < j {
            if word[i] == word[j] {
                i++
                j--
            } else {
                palindrome = false
                break
            }
        }

        if palindrome {
            return word
        }
    }
    return ""
}
