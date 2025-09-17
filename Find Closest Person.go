func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
func findClosest(x int, y int, z int) int {
    xz := abs(x-z)
    yz := abs(y-z)
    switch {
        case xz == yz:
            return 0
        case xz > yz:
            return 2
        default:
            return 1
    }
}