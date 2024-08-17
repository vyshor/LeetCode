func countSubarrays(nums []int, k int) int64 {
    n := len(nums)
    maxx := 0
    for _, num := range nums {
        maxx = max(maxx, num)
    }

    prefixes := make([]int, 0)
    suffixes := make([]int, 0)
    count := 0
    total := 0
    for i := 0; i < n; i++ {
        count++
        if nums[i] == maxx {
            prefixes = append(prefixes, count)
            count = 0
            total++
        }
    }

    if total < k {
        return 0
    }

    for i := n-1; i > -1; i-- {
        if nums[i] == maxx {
            suffixes = append(suffixes, n-i)
        }
    }

    var summ int64
    for i := 0; i < total-k+1; i++ {
        summ += int64(prefixes[i]) * int64(suffixes[total-k-i])
    }
    return summ
}

