func minDays(bloomDay []int, m int, k int) int {
    n := len(bloomDay)
    if n / k < m {
        return -1
    }

    check := func(day int) bool {
        bouquet := 0
        streak := 0
        for i := 0; i < n; i++ {
            if bloomDay[i] <= day {
                streak++
                if streak == k {
                    bouquet++
                    streak = 0
                    if bouquet == m {
                        return true
                    }
                }
            } else {
                streak = 0
            }
        }
        return false
    }

    left := bloomDay[0]
    right := bloomDay[0]
    for _, num := range bloomDay {
        left = min(left, num)
        right = max(right, num)
    }

    minn := right
    for left < right {
        mid := (left+right) / 2
        if check(mid) {
            right = mid
            minn = min(minn, mid)
        } else {
            if mid == left {
                break
            }
            left = mid
        }
    }
    return minn
}
