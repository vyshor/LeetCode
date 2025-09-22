func maximumLength(nums []int) int {
    var odd_start_alt, odd_start_const, even_start_const int
    even_start_alt := 1
    for _, num := range nums {
        odd_start_alt += (odd_start_alt ^ num) & 1
        even_start_alt += (even_start_alt ^ num) & 1
        odd_start_const += num & 1
        even_start_const += (num ^ 1) & 1
    }
    return slices.Max([]int{odd_start_alt, even_start_alt-1, odd_start_const, even_start_const, 2})
}