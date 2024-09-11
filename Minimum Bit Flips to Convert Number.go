func minBitFlips(start int, goal int) int {
    count := 0
    val := start ^ goal
    for val > 0 {
        count += val % 2
        val >>= 1
    }
    return count
}
