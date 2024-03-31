func isPossibleDivide(nums []int, k int) bool {
    counter := make(map[int]int)
    for _, num := range nums {
        if _, ok := counter[num]; !ok {
            counter[num] = 1
        } else {
            counter[num]++
        }
    }
    for len(counter) > 0 {
        smallest := -1
        for num := range counter {
            if smallest == -1 {
                smallest = num
            } else {
                smallest = min(smallest, num)
            }
        }

        for num := smallest; num < smallest+k; num++ {
            if _, ok := counter[num]; !ok {
                return false
            }

            counter[num]--
            if counter[num] == 0 {
                delete(counter, num)
            }
        }
    }
    return true
}
