func sortColors(nums []int)  {
    n := len(nums)
    pt0, pt2 := 0, n-1
    for pt2 >= 0 && nums[pt2] == 2 {
        pt2--
    }

    for pt0 < n && nums[pt0] == 0 {
        pt0++
    }
    pt1 := pt0
    for pt1 <= pt2 {
        if nums[pt1] == 2 {
            nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
            pt2--
        } else if nums[pt1] == 0 {
            if pt1 == pt0 {
                pt1++
                pt0++
            } else {
                nums[pt1], nums[pt0] = nums[pt0], nums[pt1]
                pt0++
            }
        } else {
            pt1++
        }
    }
}
