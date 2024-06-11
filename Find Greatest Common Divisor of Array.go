func gcd(a, b int) int {
    if a == 0 {
        return b
    }
    return gcd(b % a, a)
}

func findGCD(nums []int) int {
    return gcd(slices.Min(nums), slices.Max(nums))
}
