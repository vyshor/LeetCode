func maximumUniqueSubarray(nums []int) int {
    prev := make(map[int]int)
    maxx := 0
    summ := 0
    left_ptr := 0
    right_ptr := 0
    n := len(nums)
    for right_ptr < n {
        num := nums[right_ptr]
        if idx, ok := prev[num]; ok {
            for i := left_ptr; i < idx+1; i++ {
                summ -= nums[i]
            }
            left_ptr = max(left_ptr, idx+1)
        }
        summ += num
        maxx = max(maxx, summ)
        prev[num] = right_ptr
        right_ptr++
    }
    return maxx
}
