func maxSum(nums []int) int {
    seen := make(map[int]interface{})
    summ := 0
    maxx := nums[0]

    for _, num := range nums {
        if num > 0 {
            if _, ok := seen[num]; !ok {
                summ += num
                seen[num] = nil
            }
        }
        maxx = max(maxx, num)
    }

    if len(seen) == 0 {
        return maxx
    }
    return summ
}