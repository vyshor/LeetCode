func getMaximumXor(nums []int, maximumBit int) []int {
    xorr := 0
    maxx := (1 << maximumBit) - 1
    n := len(nums)
    ans := make([]int, 0)
    for _, num := range nums {
        xorr ^= num
    }
    for i := n-1; i > -1; i-- {
        ans = append(ans, (xorr & maxx) ^ maxx)
        xorr ^= nums[i]
    }
    return ans
}
