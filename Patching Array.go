func minPatches(nums []int, n int) int {
    var i, ans, total int
    m := len(nums)
    j := 1
    for j <= n {
        for i < m && nums[i] <= j {
            total += nums[i]
            i++
        }

        if total < j {
            ans++
            total += j
        }
        j = total+1
    }
    return ans
}

