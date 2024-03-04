func minimumOneBitOperations(n int) int {
    binary := n
    for n > 0 {
        n >>= 1
        binary ^= n
    }
    return binary
}
