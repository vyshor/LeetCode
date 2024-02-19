func isPowerOfTwo(n int) bool {
    if n == 0 {
        return false
    }
    return n & (n-1) == 0
}

// func isPowerOfTwo(n int) bool {
//     single_one := 0
//     for n > 0 {
//         if n & single_one == 1 {
//             return false
//         }
//         single_one |= n & 1
//         n >>= 1
//     }
//     return single_one == 1
}
