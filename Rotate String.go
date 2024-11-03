func rotateString(s string, goal string) bool {
    if len(s) != len(goal) {
        return false
    }
    s = s+s
    return strings.Contains(s, goal)
}
