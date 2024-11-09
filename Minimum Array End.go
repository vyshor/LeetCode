func minEnd(n int, x int) int64 {
    var ans, shift int64
    n--
    i := 0
    for n > 0 || x > 0 {
        if x & 1 == 1 {
            shift = 1
        } else {
            shift = int64(n & 1)
            n >>= 1
        }

        ans |= (shift << i)
        x >>= 1
        i++
    }
    return ans
}
