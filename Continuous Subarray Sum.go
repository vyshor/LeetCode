func add(i, j, k int) int {
    i += j
    if i < 0 {
        i += k
    }
    return i % k
}

func checkSubarraySum(nums []int, k int) bool {
    n := len(nums)
    if n == 1 {
        return false
    }
    if n == 2 {
        return add(nums[0], nums[1], k) == 0
    }

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

    seen := map[int]interface{} {
        0: nil,
    }

    for i := 2; i < n+1; i++ {
        finding := add(total, -suffixes[i], k)
        if _, ok := seen[finding]; ok {
            return true
        }
        seen[prefixes[i-2]] = nil
    }
    return false
}

