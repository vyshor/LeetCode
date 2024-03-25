func findDuplicates(nums []int) []int {
    ans := make([]int, 0)
    n := len(nums)
    for _, num := range nums {
        num %= n
        if num == 0 {
            num = n
        }
        if nums[num-1] > n {
            ans = append(ans, num)
        } else {
            nums[num-1] += n
        }
    }
    return ans
}
