func averageWaitingTime(customers [][]int) float64 {
    t0 := 0
    total := 0
    for _, customer := range customers {
        a, t := customer[0], customer[1]
        if t0 <= a {
            total += t
            t0 = a+t
        } else {
            total += (t0-a) + t
            t0 = t0+t
        }
    }
    return float64(total)/float64(len(customers))
}
