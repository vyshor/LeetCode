func subsets(nums []int) [][]int {
    n := len(nums)
    subsets := make([][]int, 0)
    arr := make([]int, 0)
    var explore func(i int)
    explore = func(i int) {
        if i == n {
            new_arr := append([]int{}, arr...)
            subsets = append(subsets, new_arr)
            return
        }

        explore(i+1)

        arr = append(arr, nums[i])
        explore(i+1)
        arr = arr[:len(arr)-1]
    }
    explore(0)
    return subsets
}
