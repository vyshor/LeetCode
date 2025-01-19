func xorAllNums(nums1 []int, nums2 []int) int {
    n1 := len(nums1)
    n2 := len(nums2)
    ans := 0
    if n1 % 2 == 1 {
        for _, num := range nums2 {
            ans ^= num
        }
    }

    if n2 % 2 == 1 {
        for _, num := range nums1 {
            ans ^= num
        }
    }
    return ans
}
