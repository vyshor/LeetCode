func minOperations(nums []int, k int) int {
    for _, num := range nums {
        k ^= num
    }
    var count int
    for k > 0 {
        count += k % 2
        k >>= 1
    }
    return count
}
