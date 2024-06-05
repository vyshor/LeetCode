func longestPalindrome(s string) int {
    var odd_count, even_count int
    counter := make(map[rune]int)
    for _, c := range s {
        if _, ok := counter[c]; !ok {
            counter[c] = 1
        } else {
            counter[c]++
        }

        if counter[c] % 2 == 0 {
            even_count++
            odd_count--
        } else {
            odd_count++
        }
    }

    if odd_count > 1 {
        odd_count = 1
    }

    return even_count * 2 + odd_count
}
