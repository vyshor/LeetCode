func judgeSquareSum(c int) bool {
    if c == 0 {
        return true
    }

    dp := make(map[int]interface{})
    i := 0
    for {
        sq := i*i
        if sq == c {
            return true
        } else if sq > c {
            break
        }
        dp[sq] = nil
        if _, ok := dp[c-sq]; ok {
            return true
        }
        i++
    }
    return false
}
