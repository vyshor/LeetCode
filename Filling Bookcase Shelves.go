func key(book int, j int) int {
    return book << 10 | j
}

func minHeightShelves(books [][]int, shelfWidth int) int {
    n := len(books)
    dp := make(map[int]int)
    var place func(int, int, int) int
    place = func(book int, j int, h int) int {
        k := key(book, j)
        if val, ok := dp[k]; ok {
            return val
        }

        if book == n {
            return h
        }

        thic, height := books[book][0], books[book][1]
        cost := 1 << 32
        if j + thic <= shelfWidth {
            cost = place(book+1, j+thic, max(height, h))
        }

        if j != 0 {
            cost = min(cost, h+place(book, 0, 0))
        }

        dp[k] = cost
        return cost
    }

    ans := place(0, 0, 0)
    return ans
}
