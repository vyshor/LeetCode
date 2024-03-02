func sortedSquares(nums []int) []int {
    i := 0
    j := len(nums) - 1
    arr := make([]int, 0)
    sq_i := nums[i]*nums[i]
    sq_j := nums[j]*nums[j]
    for i < j {
        if sq_i > sq_j {
            arr = append(arr, sq_i)
            i++
            sq_i = nums[i]*nums[i]
        } else {
            arr = append(arr, sq_j)
            j--
            sq_j = nums[j]*nums[j]
        }
    }

    arr = append(arr, sq_i)
    i = 0
    j = len(arr) - 1
    for i < j {
        val := arr[i]
        arr[i] = arr[j]
        arr[j] = val
        i++
        j--
    }
    return arr
}
