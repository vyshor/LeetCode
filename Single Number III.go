func singleNumber(nums []int) []int {
    xor := 0
    for _, num := range nums {
        xor ^= num
    }

    xor2 := xor
    first_diff := 0
    for xor2 % 2 == 0 {
        first_diff++
        xor2 >>= 1
    }

    xor2 = 0
    for _, num := range nums {
        if (1 << first_diff) & num > 0 {
            xor2 ^= num
        }
    }
    xor ^= xor2
    return []int{xor, xor2}
}
