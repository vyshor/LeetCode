func maxOperations(nums []int) int {
    i := 2
    n := len(nums)
    summ := nums[0] + nums[1]
    count := 1
    for i+1 < n {
        if nums[i] + nums[i+1] == summ  {
            count++
            i += 2
        } else {
            break
        }
    }
    return count
}
