func add(i, j, k int) int {
    i += j
    for i < 0 {
        i += k
    }
    return i % k
}

func subarraysDivByK(nums []int, k int) int {
    n := len(nums)
    prefixes := make([]int, n)
    suffixes := make([]int, n+1)
    total := 0
    for i := 0; i < n; i++ {
        total = add(total, nums[i], k)
        prefixes[i] = total
    }

    t := 0
    for i := n-1; i >= 0; i-- {
        t = add(t, nums[i], k)
        suffixes[i] = t
    }

    count := 0
    seen := map[int]int {
        0: 1,
    }

    for i := 1; i < n+1; i++ {
        finding := add(total, -suffixes[i], k)
        count += seen[finding]
        seen[prefixes[i-1]]++
    }
    return count
}

