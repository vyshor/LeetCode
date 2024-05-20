func subsetXORSum(nums []int) int {
    n := len(nums)
    var total, xor int
    var explore func(int)
    explore = func(i int) {
        if i == n {
            total += xor
            return
        }

        explore(i+1)

        prev := xor
        xor ^= nums[i]

        explore(i+1)
        xor = prev
    }
    explore(0)
    return total
}
