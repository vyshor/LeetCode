func minOperations(logs []string) int {
    count := 0
    for _, log := range logs {
        if log == "../" {
            count--
            if count < 0 {
                count = 0
            }
        } else if log != "./" {
            count++
        }
    }
    return count
}
