func canBeValid(s string, locked string) bool {
    n := len(s)
    if n % 2 == 1 {
        return false
    }

    var opens, unlocked int
    for i := 0; i < n; i++ {
        if locked[i] == '1' {
            if s[i] == '(' {
                opens++
            } else {
                if opens > 0 {
                    opens--
                } else if unlocked > 0 {
                    unlocked--
                } else{
                    return false
                }
            }
        } else {
            unlocked++
        }
    }

    unlocked = 0
    opens = 0
    for i := n-1; i >= 0; i-- {
        if locked[i] == '1' {
            if s[i] == ')' {
                opens++
            } else {
                if opens > 0 {
                    opens--
                } else if unlocked > 0 {
                    unlocked--
                } else{
                    return false
                }
            }
        } else {
            unlocked++
        }
    }
    return true
}
