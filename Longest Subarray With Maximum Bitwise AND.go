func longestSubarray(nums []int) int {
    count := 0
    maxx := 0
    k := 0
    for _, num := range nums {
        if num > k {
            k = num
            count = 1
            maxx = 1
        } else if num == k {
            count++
            maxx = max(maxx, count)
        } else {
            count = 0
        }
    }
    return maxx
}
