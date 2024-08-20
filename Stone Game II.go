func stoneGameII(piles []int) int {
    dp := make(map[int64]int)
    n := len(piles)
    key := func(i, turn, m int) int64 {
        k := int64(m)
        k <<= 1
        k |= int64(turn)
        k <<= 10
        k |= int64(i)
        return k
    }

    var maximise func(int, int, int) int
    maximise = func(i, turn, m int) int {
        if (i == n) {
            return 0
        }

        k := key(i, turn, m)
        if val, ok := dp[k]; ok {
            return val
        }

        maxx := math.MinInt32;
        summ := 0
        for j := 0; j < m*2; j++ {
            if i+j >= n {
                break
            }
            summ += piles[i+j]
            maxx = max(maxx, summ - maximise(i+j+1, 1 ^ turn, max(m,j+1)))
        }
        dp[k] = maxx
        return maxx
    }

    total := 0
    for _, pile := range piles {
        total += pile
    }
    max_diff := maximise(0, 1, 1)
    if max_diff > 0 {
        return (total - max_diff) / 2 + max_diff
    }
    return (total + max_diff) / 2
}
