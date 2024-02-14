func rearrangeArray(nums []int) []int {
    n := len(nums)
    arr := make([]int, 0, n)
    pos := true
    var i, j int
    for nums[i] < 0 {
        i++
    }
    for nums[j] > 0 {
        j++
    }
    for i < n || j < n {
        if pos {
            arr = append(arr, nums[i])
            i++
            for i < n && nums[i] < 0 {
                i++
            }
        } else {
            arr = append(arr, nums[j])
            j++
            for j < n && nums[j] > 0 {
                j++
            }
        }
        pos = !pos
    }
    return arr
}
