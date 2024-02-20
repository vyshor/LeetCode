func missingNumber(nums []int) int {
    n := len(nums)
    nums = append(nums, 0)
    for i:=0;i<n;i++ {
        nums[nums[i] % (n+1)] += n+1
    }

    for i, num := range nums {
        if num < (n+1) {
            return i
        }
    }
    return n
}
