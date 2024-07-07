func numWaterBottles(numBottles int, numExchange int) int {
    var count, remainder int
    for numBottles > 0 {
        count += numBottles
        numBottles += remainder
        remainder = numBottles % numExchange
        numBottles /= numExchange
    }
    return count
}
