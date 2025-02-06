func maxAscendingSum(nums []int) int {
    n := len(nums)
    maxx := nums[0]
    summ := nums[0]
    for i := 1; i < n; i++ {
        if nums[i] > nums[i-1] {
            summ += nums[i]
        } else {
            summ = nums[i]
        }
        maxx = max(maxx, summ)
    }
    return maxx
}