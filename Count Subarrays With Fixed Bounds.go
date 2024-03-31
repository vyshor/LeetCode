func countSubarrays(nums []int, minK int, maxK int) int64 {
    n := len(nums)
    var count int64
    var left, right int
    prev_max := -1
    prev_min := -1
    for right < n {
        num := nums[right]
        if num > maxK || num < minK {
            right++
            left = right
            prev_max = -1
            prev_min = -1
            continue
        }

        if num == maxK {
            prev_max = right
        }

        if num == minK {
            prev_min = right
        }

        if prev_max != -1 && prev_min != -1 {
            count += int64(min(prev_max, prev_min) - left + 1)
        }

        right++
    }
    return count
}
