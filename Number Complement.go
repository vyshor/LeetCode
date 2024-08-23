func findComplement(num int) int {
    var i, ans int
    for num > 0 {
        if num % 2 == 0 {
            ans |= (1 << i)
        }
        i++
        num >>= 1
    }
    return ans
}
