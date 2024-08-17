func maxScoreSightseeingPair(values []int) int {
    var maxx0, maxx1 int
    for _, val := range values {
        maxx0, maxx1 = max(maxx0-1, val), max(maxx1, val+maxx0-1)
    }
    return maxx1
}
