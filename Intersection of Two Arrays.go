func intersection(nums1 []int, nums2 []int) []int {
    dp := make(map[int]interface{})
    for _, num := range nums1 {
        dp[num] = nil
    }

    arr := make([]int, 0)
    for _, num := range nums2 {
        if _, ok := dp[num]; ok {
            arr = append(arr, num)
            delete(dp, num)
        }
    }
    return arr
}
