func pivotInteger(n int) int {
    if n == 1 {
        return 1
    }

    left := 1
    right := n
    var lsum, rsum int
    for lsum < rsum || left < right-1 {
        lsum += left
        left++
        if lsum > rsum {
            rsum += right
            right--
        }
    }

    if lsum == rsum && left == right {
        return left
    }
    return -1
}
