func findKthBit(n int, k int) byte {
    var recur func(m, j int) bool
    recur = func(m, j int) bool {
        if j == 1 {
            return false
        }

        x := 1 << (m-1)
        if j == x {
            return true
        }
        if j > x {
            return !recur(m-1, 2*x-j)
        }

        y := j
        for i := 1; i < m; i++ {
            minus := 1 << (i-1)
            if y - minus <= 0 {
                return recur(i, j)
            }
            y -= minus
        }
        return false
    }

    if recur(n, k) {
        return '1'
    }
    return '0'
}
