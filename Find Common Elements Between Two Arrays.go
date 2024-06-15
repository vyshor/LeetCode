func count(nums []int) map[int]int {
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num]++
    }
    return counter
}

func findIntersectionValues(nums1 []int, nums2 []int) []int {
    counter1 := count(nums1)
    counter2 := count(nums2)
    var a1, a2 int
    for num, count := range counter1 {
        if _, ok := counter2[num]; ok {
            a1 += count
        }
    }

    for num, count := range counter2 {
        if _, ok := counter1[num]; ok {
            a2 += count
        }
    }
    return []int{a1, a2}
}
