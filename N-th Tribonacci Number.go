func tribonacci(n int) int {
    if n < 2 {
        return n
    }

    if n == 2 {
        return 1
    }

    n1 := 0
    n2 := 1
    n3 := 1
    for i := 0; i < n-2; i++ {
        n4 := n1+n2+n3
        n1 = n2
        n2 = n3
        n3 = n4
    }
    return n3
}
