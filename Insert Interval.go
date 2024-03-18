func insert(intervals [][]int, newInterval []int) [][]int {
    low := newInterval[0]
    high := newInterval[1]

    var merged bool
    ans := make([][]int, 0)
    for _, interval := range intervals {
        if interval[1] < low  {
            ans = append(ans, interval)
            continue
        }
        if interval[0] > high {
            if !merged {
                ans = append(ans, []int{low, high})
                merged = true
            }
            ans = append(ans, interval)
        }

        if !merged {
            high = max(high, interval[1])
            low = min(low, interval[0])
        }
    }

    if !merged {
        ans = append(ans, []int{low, high})
    }

    return ans
}
