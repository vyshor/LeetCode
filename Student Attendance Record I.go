func checkRecord(s string) bool {
    absent := 0
    late := 0
    r := []rune(s)
    for _, c := range r {
        if c == 'L' {
            late++
            if late == 3 {
                return false
            }
        } else {
            late = 0
            if c == 'A' {
                absent++
            }
        }
    }
    return absent <= 1
}
