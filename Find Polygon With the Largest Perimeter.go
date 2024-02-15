func largestPerimeter(nums []int) int64 {
    slices.Sort(nums)
    n := len(nums)

    var summ int
    for _, num := range nums {
        summ += num
    }
    summ -= nums[n-1]

    for i := n-1; i > 1; i-- {
        if summ > nums[i] {
            return int64(summ + nums[i])
        } else {
            summ -= nums[i-1]
        }
    }
    return -1
}
