func timeRequiredToBuy(tickets []int, k int) int {
    n := len(tickets)
    pass_k := false
    total := 0
    for i := 0; i < n; i++ {
        if pass_k {
            total += min(tickets[i], tickets[k]-1)
        } else {
            total += min(tickets[i],tickets[k])
        }

        if i == k {
            pass_k = true
        }
    }
    return total
}
