func lemonadeChange(bills []int) bool {
    c0 := 0
    c1 := 0
    for _, bill := range bills {
        if bill == 5 {
            c0++
        } else if bill == 10 {
            if c0 == 0 {
                return false
            }
            c0--
            c1++
        } else {
            if c1 >= 1 && c0 > 0 {
                c1--
                c0--
            } else if c0 >= 3 {
                c0 -= 3
            } else {
                return false
            }
        }
    }
    return true
}
