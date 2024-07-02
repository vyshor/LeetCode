func intersect(nums1 []int, nums2 []int) []int {
    counter := make(map[int]int)
    for _, num := range nums1 {
        counter[num]++
    }

    ans := make([]int, 0)
    for _, num := range nums2 {
        if counter[num] > 0 {
            ans = append(ans, num)
            counter[num]--
        }
    }

    return ans
}
