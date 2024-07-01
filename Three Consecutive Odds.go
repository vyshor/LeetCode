func threeConsecutiveOdds(arr []int) bool {
    count := 0
    for _, num := range arr {
        count = (count + num % 2) * (num % 2)
        if count == 3 {
            return true
        }
    }
    return false
}
