func maxDistance(position []int, m int) int {
    sort.Ints(position)
    n := len(position)

    check := func(min_dist int) bool {
        prev := position[0]
        baskets := m-1
        for i := 1; i < n; i++ {
            if position[i] - prev >= min_dist {
                baskets--
                prev = position[i]
            }
        }
        return baskets <= 0
    }

    left, right := 1, (position[n-1]-position[0]) / (m-1) + 1
    maxx := 1
    for left < right {
        mid := (left+right) / 2
        if check(mid) {
            maxx = max(maxx, mid)
            if left == mid {
                return maxx
            }
            left = mid
        } else {
            right = mid
        }
    }
    return maxx
}
