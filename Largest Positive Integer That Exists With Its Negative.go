func findMaxK(nums []int) int {
    seen := make(map[int]interface{})
    maxx := -1
    for _, num := range nums {
        seen[num] = nil
        if _, ok := seen[-num]; ok {
            if num < 0 {
                num *= -1
            }
            maxx = max(maxx, num)
        }
    }
    return maxx
}
