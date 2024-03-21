func numRabbits(answers []int) int {
    counter := make(map[int]int)
    for _, num := range answers {
        if _, ok := counter[num]; !ok {
            counter[num] = 1
        } else {
            counter[num]++
        }
    }

    total := 0
    for num, count := range counter {
        total += int(math.Ceil(float64(count) / float64(num + 1))) * (num + 1)
    }
    return total
}

