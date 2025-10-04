func maxArea(height []int) int {
    n := len(height)
    left, right := 0, n-1
    maxx := 0
    for left < right {
        maxx = max(maxx, (right-left)*min(height[left], height[right]))
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }
    return maxx
}