func lengthOfLastWord(s string) int {
    count := 0
    have_space := true
    for _, c := range s {
        if c == ' ' {
            have_space = true
        } else if have_space {
            count = 1
            have_space = false
        } else {
            count++
        }
    }
    return count
}
