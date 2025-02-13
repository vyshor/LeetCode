func max3(x0, x1, x2 int) []int {
    if (x0 <= x1 && x0 <= x2) {return []int{x1, x2}}
    if (x1 <= x0 && x1 <= x2) {return []int{x0, x2}}
    return []int{x0, x1}
}

func maximumSum(nums []int) int {
    matches := make(map[int][]int)
    maxx := -1
    for _, num := range nums {
        summ := 0
        x := num
        for x > 0 {
            summ += x % 10
            x /= 10
        }

        if v, ok := matches[summ]; ok {
            matches[summ] = max3(v[0], v[1], num)
            maxx = max(maxx, matches[summ][0] + matches[summ][1])
        } else {
            matches[summ] = []int{num, 0}
        }
    }
    return maxx
}
