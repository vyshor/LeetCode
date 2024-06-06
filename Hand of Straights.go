func isNStraightHand(hand []int, groupSize int) bool {
    sort.Ints(hand)
    counter := make(map[int]int)
    for _, num := range hand {
        if _, ok := counter[num]; !ok {
            counter[num] = 1
        } else {
            counter[num]++
        }
    }
    for _, num := range hand {
        if counter[num] > 0 {
            for i := num; i < num+groupSize; i++ {
                counter[i]--
                if counter[i] < 0 {
                    return false
                }
            }
        }
    }
    return true
}
