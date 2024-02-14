func maxFrequencyElements(nums []int) int {
    counter := make(map[int]int)
    var maxx, max_count int
    for _, num := range nums {
        if _, ok := counter[num]; ok {
            counter[num]++
        } else {
            counter[num] = 1
        }

        val := counter[num]
        if val > maxx {
            maxx = val
            max_count = 1
        } else if val == maxx {
            max_count++
        }
    }
    return maxx * max_count
}
