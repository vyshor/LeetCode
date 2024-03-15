func getCommon(nums1 []int, nums2 []int) int {
    var p1, p2 int
    n1 := len(nums1)
    n2 := len(nums2)
    for nums1[p1] != nums2[p2] {
        for p1 < n1 && nums1[p1] < nums2[p2] {
            p1++
        }

        if p1 == n1 {
            return -1
        }

        for p2 < n2 && nums2[p2] < nums1[p1] {
            p2++
        }

        if p2 == n2 {
            return -1
        }
    }

    if nums1[p1] == nums2[p2] {
        return nums1[p1]
    }

    return -1
}
