var dp = map[int]int{0:1, 1:1, 2:2}

func recur(r int) int {
    if v, ok := dp[r]; ok {
        return v
    }

    summ := 0;
    for i := 0; i < r; i++ {
        summ += recur(i) * recur(r-i-1)
    }
    dp[r] = summ
    return summ
}

func numTrees(n int) int {
    return recur(n)
}
