func firstMissingPositive(nums []int) int {
    n := len(nums)
    for i, num := range nums {
        if num > n || num <= 0 {
            nums[i] = n+1
        }
    }

    for _, num := range nums {
        abs_num := num
        if abs_num < 0 {
            abs_num *= -1
        }

        if abs_num <= n {
            if nums[abs_num-1] > 0 {
                nums[abs_num-1] *= -1
            }
        }
    }

    for i, num := range nums {
        if num > 0 {
            return i+1
        }
    }
    return n+1
}
