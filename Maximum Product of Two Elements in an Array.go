func maxProduct(nums []int) int {
    var maxx, maxx2 int
    for _, num := range nums {
        if num >= maxx {
            maxx2 = maxx
            maxx = num
        } else if num > maxx2 {
            maxx2 = num
        }
    }
    return (maxx-1)*(maxx2-1)
}
