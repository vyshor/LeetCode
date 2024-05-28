func abs(i int) int {
    if i < 0 {
        return -i
    }
    return i
}

func equalSubstring(s string, t string, maxCost int) int {
    var left, right, cost, maxx int
    sb := []rune(s)
    tb := []rune(t)
    costs := make([]int, 0)
    n := len(s)
    for right < n {
        costs = append(costs, abs((int) (sb[right]-tb[right])))
        cost += costs[right]

        for cost > maxCost {
            cost -= costs[left]
            left += 1
        }

        right += 1
        maxx = max(maxx, right-left)
    }
    return maxx
}
