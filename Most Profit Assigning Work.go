type Pair struct {
    difficulty int
    profit int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    q := make([]Pair, 0)
    n := len(profit)
    min_difficulty := 1 << 17
    max_profit := 0
    for i := 0; i < n; i++ {
        min_difficulty = min(min_difficulty, difficulty[i])
        max_profit = max(max_profit, profit[i])
        q = append(q, Pair{difficulty: difficulty[i], profit: -profit[i]})
    }

    sort.Slice(q, func(i, j int) bool {
                        if q[i].difficulty == q[j].difficulty {
                            return q[i].profit < q[j].profit
                        }
                        return q[i].difficulty < q[j].difficulty
                    })

    maxx := 0
    for i := 0; i < n; i++ {
        maxx = min(maxx, q[i].profit)
        q[i].profit = maxx
    }

    total := 0
    for _, w := range worker {
        if w < min_difficulty {
            continue
        }

        i := sort.Search(len(q), func(i int) bool { return q[i].difficulty >= w })
        if i < n && w == q[i].difficulty {
            total -= q[i].profit
        } else {
            total -= q[i-1].profit
        }
    }
    return total
}

